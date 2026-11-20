"""Reproducible synthetic cybersecurity experiment and portable forest export."""
from pathlib import Path
import json, csv
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'; OUT.mkdir(exist_ok=True)
FEATURES=['packet_bytes','duration_ms','packets_per_second','failed_logins','unique_ports','outbound_kb','syn_ratio','error_rate']
LABELS=['Normal','DDoS pattern','Port scan pattern','Brute force pattern','Exfiltration pattern']
def generate(n=6000,seed=42):
 rng=np.random.default_rng(seed); y=rng.choice(5,n,p=[.72,.08,.07,.07,.06])
 rows=[]
 for c in y:
  x=[rng.normal(650,240),rng.lognormal(6.4,1),rng.lognormal(3.2,.7),rng.poisson(.4),rng.poisson(3)+1,rng.lognormal(4,1.1),rng.beta(2,9),rng.beta(1,12)]
  # Overlapping distributions, including busy normal services and subtle anomalies.
  if c==0 and rng.random()<.12: x[2]*=5; x[5]*=5; x[4]+=8
  if c==1: x[2]=rng.lognormal(5.3,.85); x[6]=rng.beta(5,3); x[1]*=.3
  if c==2: x[4]=rng.poisson(18)+3; x[7]=rng.beta(3,5); x[0]*=.55
  if c==3: x[3]=rng.poisson(5)+1; x[7]=rng.beta(3,5); x[4]=rng.poisson(2)+1
  if c==4: x[5]=rng.lognormal(6.7,1); x[0]=rng.normal(1100,230); x[1]*=3
  rows.append([round(max(0,v),4) for v in x])
 return np.asarray(rows),y

def metrics(y,p):
 pred=p>=.5
 return dict(accuracy=accuracy_score(y,pred),precision=precision_score(y,pred,zero_division=0),recall=recall_score(y,pred,zero_division=0),f1=f1_score(y,pred,zero_division=0),roc_auc=roc_auc_score(y,p),confusion=confusion_matrix(y,pred).tolist())

def main():
 X,kind=generate(); y=(kind>0).astype(int); idx=np.arange(len(y))
 tr,te=train_test_split(idx,test_size=.2,random_state=42,stratify=kind)
 rf=RandomForestClassifier(n_estimators=40,max_depth=8,min_samples_leaf=4,class_weight='balanced',random_state=42,n_jobs=1).fit(X[tr],y[tr])
 models={'Random Forest':rf,'Decision Tree':DecisionTreeClassifier(max_depth=8,min_samples_leaf=4,random_state=42).fit(X[tr],y[tr]),'Logistic Regression':make_pipeline(StandardScaler(),LogisticRegression(max_iter=1000,random_state=42)).fit(X[tr],y[tr])}
 result={name:metrics(y[te],m.predict_proba(X[te])[:,1]) for name,m in models.items()}
 trees=[]
 for estimator in rf.estimators_:
  t=estimator.tree_; vals=t.value[:,0,:]; probs=(vals[:,1]/vals.sum(axis=1)).tolist()
  trees.append(dict(left=t.children_left.tolist(),right=t.children_right.tolist(),feature=t.feature.tolist(),threshold=t.threshold.tolist(),probability=probs))
 model=dict(features=FEATURES,trees=trees,importance=rf.feature_importances_.tolist(),version='sentinel-rf-1.0',seed=42,training_rows=len(tr),test_rows=len(te),metrics=result,labels=LABELS)
 (OUT/'model.json').write_text(json.dumps(model,separators=(',',':')))
 records=[]
 p=rf.predict_proba(X[te])[:,1]
 for k,i in enumerate(te): records.append(dict(id=f'FLOW-{k+1:05d}',values=X[i].tolist(),label=int(y[i]),scenario=LABELS[kind[i]],probability=float(p[k])))
 (OUT/'evaluation.json').write_text(json.dumps(records,separators=(',',':')))
 for name,indices in [('synthetic_dataset.csv',idx),('sample_traffic.csv',te[:150])]:
  with (OUT/name).open('w',newline='') as f:
   w=csv.writer(f); w.writerow(FEATURES+['label','scenario'])
   for i in indices:w.writerow(list(X[i])+[int(y[i]),LABELS[kind[i]]])
 (ROOT/'ml'/'metrics.json').write_text(json.dumps(result,indent=2))
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
