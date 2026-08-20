#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from validate_candidate2_contracts import validate_support, validate_obligation, validate_recovery


def claim(cid, instance):
    return {
        'claim_id': cid,
        'scope': {'host':'host-a','runtime_instance':instance,'configuration':'cfg-15s','epoch':'e1','time_interval':'t1'}
    }


def main():
    cases = []

    c1 = claim('claim-001','gw-a')
    s1 = {
        'claim_ref':'claim-001','support_status':'SUPPORTS',
        'observed_scope':c1['scope'],'claimed_scope':c1['scope'],
        'transfer_basis':{'required':False,'type':None,'evidence_refs':[]}
    }
    cases.append(('same-scope support', validate_support(c1,s1), True, 'SUPPORT_SCOPE_DIRECT_MATCH'))

    c2 = claim('claim-002','gw-b')
    observed = {'host':'host-a','runtime_instance':'gw-a','configuration':'cfg-15s','epoch':'e1','time_interval':'t1'}
    s2 = {'claim_ref':'claim-002','support_status':'SUPPORTS','observed_scope':observed,'claimed_scope':c2['scope'],
          'transfer_basis':{'required':False,'type':None,'evidence_refs':[]}}
    cases.append(('cross-instance without transfer', validate_support(c2,s2), False, 'TRANSFER_EVIDENCE_REQUIRED'))

    s3 = dict(s2)
    s3['transfer_basis']={'required':True,'type':'EQUIVALENCE','evidence_refs':['ev-equivalence']}
    cases.append(('cross-instance with declared transfer evidence', validate_support(c2,s3), True, 'SUPPORT_SCOPE_TRANSFER_DECLARED'))

    o1 = {'trigger':{'observed':True},'materiality':'MATERIAL','status':'PENDING','required_before_claim_refs':['workflow-complete']}
    cases.append(('pending material obligation', validate_obligation(o1), False, 'MATERIAL_OBLIGATION_BLOCKS_CLAIM'))

    o2 = {'trigger':{'observed':True},'materiality':'MATERIAL','status':'SATISFIED','required_before_claim_refs':['workflow-complete'],
          'closure_evidence_refs':['ev-close'],'resolution_reason':'closed'}
    cases.append(('satisfied obligation with evidence', validate_obligation(o2), True, 'OBLIGATION_STATE_ACCEPTABLE'))

    r1 = {'state_restore':{'result':'SUCCESS'},'history_continuity':{'status':'UNKNOWN'},
          'recovery_claim':{'scope':'STATE_AND_HISTORY'}}
    cases.append(('state restore cannot imply history restore', validate_recovery(r1), False, 'FULL_RECOVERY_REQUIRES_PRESERVED_HISTORY'))

    r2 = {'state_restore':{'result':'SUCCESS'},'history_continuity':{'status':'PRESERVED'},
          'recovery_claim':{'scope':'STATE_AND_HISTORY'}}
    cases.append(('state+history recovery with preserved history', validate_recovery(r2), True, 'STATE_AND_HISTORY_RECOVERY_SUPPORTED'))

    failed = 0
    for name, got, expected_ok, expected_code in cases:
        ok = got.get('ok') == expected_ok and got.get('code') == expected_code
        print(('PASS' if ok else 'FAIL'), '-', name, '-', got.get('code'))
        failed += 0 if ok else 1

    print(f'\n{len(cases)-failed}/{len(cases)} tests passed')
    return 1 if failed else 0


if __name__ == '__main__':
    raise SystemExit(main())
