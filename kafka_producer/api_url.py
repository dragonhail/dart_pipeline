#정기보고서 주요정보
#지분공시 종합정보
#재무정보
annual_repo = {
    "cond_cap_sec_bal": "https://opendart.fss.or.kr/api/cndlCaplScritsNrdmpBlce.json", # 조건부 자본증권 미상환 잔액
    "exec_comp_stat": "https://opendart.fss.or.kr/api/unrstExctvMendngSttus.json", # 미등기임원 보수현황
    "corp_bond_bal": "https://opendart.fss.or.kr/api/cprndNrdmpBlce.json", # 회사채 미상환 잔액
    "short_bond_bal": "https://opendart.fss.or.kr/api/srtpdPsndbtNrdmpBlce.json", # 단기사채 미상환 잔액
    "com_paper_bal": "https://opendart.fss.or.kr/api/entrprsBilScritsNrdmpBlce.json", # 기업어음증권 미상환 잔액
    "debt_sec_perf": "https://opendart.fss.or.kr/api/detScritsIsuAcmslt.json", # 채무증권 발행실적
    "priv_fund_use": "https://opendart.fss.or.kr/api/prvsrpCptalUseDtls.json", # 사모자금의 사용내역
    "pub_fund_use": "https://opendart.fss.or.kr/api/pssrpCptalUseDtls.json", # 공모자금의 사용내역
    "dir_aud_comp_gm": "https://opendart.fss.or.kr/api/drctrAdtAllMendngSttusGmtsckConfmAmount.json", # 이사·감사 전체의 보수현황(주주총회 승인금액)
    "dir_aud_comp_type": "https://opendart.fss.or.kr/api/drctrAdtAllMendngSttusMendngPymntamtTyCl.json", # 이사·감사 전체의 보수현황(보수지급금액 - 유형별)
    "total_shares": "https://opendart.fss.or.kr/api/stockTotqySttus.json", # 주식의 총수 현황 /
    "auditor_name_op": "https://opendart.fss.or.kr/api/accnutAdtorNmNdAdtOpinion.json", # 회계감사인의 명칭 및 감사의견
    "audit_serv_contr": "https://opendart.fss.or.kr/api/adtServcCnclsSttus.json", # 감사용역체결현황
    "non_audit_contr": "https://opendart.fss.or.kr/api/accnutAdtorNonAdtServcCnclsSttus.json", # 회계감사인과의 비감사용역 계약체결 현황
    "out_dir_stat": "https://opendart.fss.or.kr/api/accnutAdtorNonAdtServcCnclsSttus.json", # 사외이사 및 그 변동현황 /
    "new_cap_sec_bal": "https://opendart.fss.or.kr/api/newCaplScritsNrdmpBlce.json", # 신종자본증권 미상환 잔액
    "cap_inc_dec_stat": "https://opendart.fss.or.kr/api/irdsSttus.json", # 증자(감자) 현황
    "dividend_info": "https://opendart.fss.or.kr/api/alotMatter.json", # 배당에 관한 사항 /
    "treasury_stock": "https://opendart.fss.or.kr/api/tesstkAcqsDspsSttus.json", # 자기주식 취득 및 처분 현황
    "major_shareholder": "https://opendart.fss.or.kr/api/hyslrSttus.json", # 최대주주 현황 /
    "major_share_chg": "https://opendart.fss.or.kr/api/hyslrChgSttus.json", # 최대주주 변동현황
    "minority_share": "https://opendart.fss.or.kr/api/mrhlSttus.json", # 소액주주 현황 /
    "exec_status": "https://opendart.fss.or.kr/api/exctvSttus.json", # 임원 현황 /
    "emp_status": "https://opendart.fss.or.kr/api/empSttus.json", # 직원 현황 /
    "indv_dir_aud_comp": "https://opendart.fss.or.kr/api/hmvAuditIndvdlBySttus.json", # 이사·감사의 개인별 보수 현황
    "all_dir_aud_comp": "https://opendart.fss.or.kr/api/hmvAuditAllSttus.json", # 이사·감사 전체의 보수현황
    "top5_exec_comp": "https://opendart.fss.or.kr/api/indvdlByPay.json", # 개인별 보수지급 금액(5억이상 상위5인) /
    "other_corp_inv": "https://opendart.fss.or.kr/api/otrCprInvstmntSttus.json", # 타법인 출자현황
    "major_stock": "https://opendart.fss.or.kr/api/majorstock.json", #대량보유 상황보고
    "exec_maj_shareown": "https://opendart.fss.or.kr/api/elestock.json", #임원ㆍ주요주주 소유보
    "single_corp_fin": "https://opendart.fss.or.kr/api/fnlttSinglIndx.json" #단일회사 주요 재무제표 /
    }