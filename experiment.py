import difflib
from common import *

def link(name,catalog):
    scores=sorted([(difflib.SequenceMatcher(None,name.lower(),x.lower()).ratio(),x) for x in catalog],reverse=True)
    if scores[0][0]<.65:return 'unknown'
    if scores[0][0]-scores[1][0]<.12:return 'ambiguous'
    return scores[0][1]
def run():
    catalog=['gateway-east','gateway-west','cache-primary','billing-prod','queue-dev']
    fixtures=[('gateway-east','gateway-east'),('gatway-east','gateway-east'),('gateway','ambiguous'),('satellite','unknown'),('cache-primary','cache-primary'),('billing-prod','billing-prod'),('queue','queue-dev')]
    outcomes=[{'query':q,'expected':y,'predicted':link(q,catalog)} for q,y in fixtures]
    return {'cases':outcomes,'accuracy':sum(x['expected']==x['predicted'] for x in outcomes)/len(outcomes),
            'checks':[check(link('gateway',catalog)=='ambiguous','Ambiguous aliases abstain'),check(link('satellite',catalog)=='unknown','Out-of-catalog input abstains')],
            'scope':'Fictional IT asset catalog; lexical entity linking with explicit abstention. No learned model or production asset discovery.'}
