export function predict(model, values) {
 if(values.length!==model.features.length || values.some(x=>!Number.isFinite(x))) throw Error('Invalid feature vector');
 values=values.map(Math.fround); // sklearn evaluates tree inputs as float32.
 let score=0;
 for(const t of model.trees){let n=0;while(t.left[n]!==-1)n=values[t.feature[n]]<=t.threshold[n]?t.left[n]:t.right[n];score+=t.probability[n];}
 return score/model.trees.length;
}
export const limits=[65535,86400000,10000000,100000,65535,1000000000,1,1];
export function validate(values){return values.length===8&&values.every((v,i)=>Number.isFinite(v)&&v>=0&&v<=limits[i]);}
export function parseCSV(text,features){
 const rows=[];let row=[],cell='',quoted=false;
 text=text.replace(/^\uFEFF/,'');
 for(let i=0;i<text.length;i++){const c=text[i];if(c==='"'){if(quoted&&text[i+1]==='"'){cell+='"';i++;}else if(!quoted&&cell!=='')throw Error('Unexpected quote in CSV');else quoted=!quoted;}else if(c===','&&!quoted){row.push(cell);cell='';}else if((c==='\n'||c==='\r')&&!quoted){if(c==='\r'&&text[i+1]==='\n')i++;row.push(cell);if(row.some(v=>v.trim()))rows.push(row);row=[];cell='';}else cell+=c;}
 if(quoted)throw Error('Unclosed quoted field');row.push(cell);if(row.some(v=>v.trim()))rows.push(row);
 if(rows.length<2)throw Error('CSV must contain a header and at least one data row');
 if(rows.length>5001)throw Error('Maximum 5,000 data rows');
 const header=rows.shift().map(x=>x.trim());if(new Set(header).size!==header.length)throw Error('Duplicate column names');
 const indices=features.map(f=>header.indexOf(f));if(indices.includes(-1))throw Error('Missing columns: '+features.filter((f,i)=>indices[i]<0).join(', '));
 return rows.map((r,j)=>{if(r.length!==header.length)throw Error(`Row ${j+2}: column count does not match header`);const vals=indices.map(i=>r[i].trim()===''?NaN:Number(r[i]));if(!validate(vals))throw Error(`Row ${j+2}: invalid, empty or out-of-range feature value`);return vals;});
}
export function evaluate(rows,threshold){let tn=0,fp=0,fn=0,tp=0;for(const r of rows){if(r.probability>=threshold){if(r.label)tp++;else fp++;}else{if(r.label)fn++;else tn++;}}const precision=tp/(tp+fp)||0,recall=tp/(tp+fn)||0;return {tn,fp,fn,tp,accuracy:(tp+tn)/rows.length,precision,recall,f1:2*precision*recall/(precision+recall)||0};}
