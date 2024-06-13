from pyspark.sql.types import StructType, StructField, StringType, ArrayType

cond_cap_sec_bal = StructType([
    StructField("rcept_no", StringType(), True),
    StructField("corp_cls", StringType(), True),
    StructField("corp_code", StringType(), True), 
    StructField("corp_name", StringType(), True),
    StructField("remndr_exprtn1", StringType(), True),
    StructField("remndr_exprtn2", StringType(), True),
    StructField("yy1_below", StringType(), True),
    StructField("yy1_excess_yy2_below", StringType(), True),
    StructField("yy2_excess_yy3_below", StringType(), True),
    StructField("yy3_excess_yy4_below", StringType(), True),
    StructField("yy4_excess_yy5_below", StringType(), True),
    StructField("yy5_excess_yy10_below", StringType(), True),
    StructField("yy10_excess_yy20_below", StringType(), True),
    StructField("yy20_excess_yy30_below", StringType(), True),
    StructField("yy30_excess", StringType(), True),
    StructField("sm", StringType(), True)
])

exec_comp_stat = StructType([
    StructField("rcept_no", StringType, nullable = true),
    StructField("corp_cls", StringType, nullable = true),
    StructField("corp_code", StringType, nullable = true),
    StructField("corp_name", StringType, nullable = true),
    StructField("se", StringType, nullable = true),
    StructField("nmpr", LongType, nullable = true),
    StructField("fyer_salary_totamt", LongType, nullable = true),
    StructField("jan_salary_am", LongType, nullable = true),
    StructField("rm", StringType, nullable = true)
  ])

corp_bond_bal = StructType([
    StructField("rcept_no", StringType(), True),
    StructField("corp_cls", StringType(), True),
    StructField("corp_code", StringType(), True),
    StructField("corp_name", StringType(), True),
    StructField("remndr_exprtn1", StringType(), True),
    StructField("remndr_exprtn2", StringType(), True),
    StructField("yy1_below", StringType(), True),
    StructField("yy1_excess_yy2_below", StringType(), True),
    StructField("yy2_excess_yy3_below", StringType(), True),
    StructField("yy3_excess_yy4_below", StringType(), True),
    StructField("yy4_excess_yy5_below", StringType(), True),
    StructField("yy5_excess_yy10_below", StringType(), True),
    StructField("yy10_excess", StringType(), True),
    StructField("sm", StringType(), True)
])

short_bond_bal = StructType([
    StructField("rcept_no", StringType(), True),
    StructField("corp_cls", StringType(), True),
    StructField("corp_code", StringType(), True),
    StructField("corp_name", StringType(), True),
    StructField("remndr_exprtn1", StringType(), True),
    StructField("remndr_exprtn2", StringType(), True),
    StructField("de10_below", StringType(), True),
    StructField("de10_excess_de30_below", StringType(), True),
    StructField("de30_excess_de90_below", StringType(), True),
    StructField("de90_excess_de180_below", StringType(), True),
    StructField("de180_excess_yy1_below", StringType(), True),
    StructField("sm", StringType(), True),
    StructField("isu_lmt", StringType(), True),
    StructField("remndr_lmt", StringType(), True)
])

com_paper_bal = StructType([
    StructField("rcept_no", StringType(), True),
    StructField("corp_cls", StringType(), True),
    StructField("corp_code", StringType(), True),
    StructField("corp_name", StringType(), True),
    StructField("remndr_exprtn1", StringType(), True),
    StructField("remndr_exprtn2", StringType(), True),
    StructField("de10_below", StringType(), True),
    StructField("de10_excess_de30_below", StringType(), True),
    StructField("de30_excess_de90_below", StringType(), True),
    StructField("de90_excess_de180_below", StringType(), True),
    StructField("de180_excess_yy1_below", StringType(), True),
    StructField("yy1_excess_yy2_below", StringType(), True),
    StructField("yy2_excess_yy3_below", StringType(), True),
    StructField("yy3_excess", StringType(), True),
    StructField("sm", StringType(), True)
])

debt_sec_perf = StructType([
    StructField("rcept_no", StringType(), True),
    StructField("corp_cls", StringType(), True),
    StructField("corp_code", StringType(), True),
    StructField("corp_name", StringType(), True),
    StructField("isu_cmpny", StringType(), True),
    StructField("scrits_knd_nm", StringType(), True),
    StructField("isu_mth_nm", StringType(), True),
    StructField("isu_de", StringType(), True),
    StructField("facvalu_totamt", StringType(), True),
    StructField("intrt", StringType(), True),
    StructField("evl_grad_instt", StringType(), True),
    StructField("mtd", StringType(), True),
    StructField("repy_at", StringType(), True),
    StructField("mngt_cmpny", StringType(), True)
])

dir_aud_comp_gm = StructType([
    StructField("rcept_no", StringType(), True),
    StructField("corp_cls", StringType(), True),
    StructField("corp_code", StringType(), True),
    StructField("corp_name", StringType(), True),
    StructField("se", StringType(), True),
    StructField("nmpr", StringType(), True),
    StructField("gmtsck_confm_amount", StringType(), True),
    StructField("rm", StringType(), True)
])

dir_aud_comp_type = StructType([
    StructField("rcept_no", StringType(), True),
    StructField("corp_cls", StringType(), True),
    StructField("corp_code", StringType(), True),
    StructField("corp_name", StringType(), True),
    StructField("se", StringType(), True),
    StructField("nmpr", StringType(), True),
    StructField("pymnt_totamt", StringType(), True),
    StructField("psn1_avrg_pymntamt", StringType(), True),
    StructField("rm", StringType(), True)
])

total_shares = StructType([
    StructField("rcept_no", StringType(), True),
    StructField("corp_cls", StringType(), True),
    StructField("corp_code", StringType(), True),
    StructField("corp_name", StringType(), True),
    StructField("se", StringType(), True),
    StructField("isu_stock_totqy", StringType(), True),
    StructField("now_to_isu_stock_totqy", StringType(), True),
    StructField("now_to_dcrs_stock_totqy", StringType(), True),
    StructField("redc", StringType(), True),
    StructField("profit_incnr", StringType(), True),
    StructField("rdmstk_repy", StringType(), True),
    StructField("etc", StringType(), True),
    StructField("istc_totqy", StringType(), True),
    StructField("tesstk_co", StringType(), True),
    StructField("distb_stock_co", StringType(), True)
])

non_audit_contr = StructType([
    StructField("rcept_no", StringType(), True),
    StructField("corp_cls", StringType(), True),
    StructField("corp_code", StringType(), True),
    StructField("corp_name", StringType(), True),
    StructField("bsns_year", StringType(), True),
    StructField("cntrct_cncls_de", StringType(), True),
    StructField("servc_cn", StringType(), True),
    StructField("servc_exc_pd", StringType(), True),
    StructField("servc_mendng", StringType(), True),
    StructField("rm", StringType(), True)
])

out_dir_stat = StructType([
    StructField("rcept_no", StringType(), True),
    StructField("corp_cls", StringType(), True),
    StructField("corp_code", StringType(), True),
    StructField("corp_name", StringType(), True),
    StructField("drctr_co", StringType(), True),
    StructField("otcmp_drctr_co", StringType(), True),
    StructField("apnt", StringType(), True),
    StructField("rlsofc", StringType(), True),
    StructField("mdstrm_resig", StringType(), True)
])

new_cap_sec_bal = StructType([
    StructField("rcept_no", StringType(), True),
    StructField("corp_cls", StringType(), True),
    StructField("corp_code", StringType(), True),
    StructField("corp_name", StringType(), True),
    StructField("remndr_exprtn1", StringType(), True),
    StructField("remndr_exprtn2", StringType(), True),
    StructField("yy1_below", StringType(), True),
    StructField("yy1_excess_yy5_below", StringType(), True),
    StructField("yy5_excess_yy10_below", StringType(), True),
    StructField("yy10_excess_yy15_below", StringType(), True),
    StructField("yy15_excess_yy20_below", StringType(), True),
    StructField("yy20_excess_yy30_below", StringType(), True),
    StructField("yy30_excess", StringType(), True),
    StructField("sm", StringType(), True)
])

cap_inc_dec_stat = StructType([
    StructField("rcept_no", StringType(), True),
    StructField("corp_cls", StringType(), True),
    StructField("corp_code", StringType(), True),
    StructField("corp_name", StringType(), True),
    StructField("isu_dcrs_de", StringType(), True),
    StructField("isu_dcrs_stle", StringType(), True),
    StructField("isu_dcrs_stock_knd", StringType(), True),
    StructField("isu_dcrs_qy", StringType(), True),
    StructField("isu_dcrs_mstvdv_fval_amount", StringType(), True),
    StructField("isu_dcrs_mstvdv_amount", StringType(), True)
])

dividend_info = StructType([
    StructField("rcept_no", StringType(), True),
    StructField("corp_cls", StringType(), True),
    StructField("corp_code", StringType(), True),
    StructField("corp_name", StringType(), True),
    StructField("se", StringType(), True),
    StructField("stock_knd", StringType(), True),
    StructField("thstrm", StringType(), True),
    StructField("frmtrm", StringType(), True),
    StructField("lwfr", StringType(), True)
])

treasury_stock = StructType([
    StructField("rcept_no", StringType(), True),
    StructField("corp_cls", StringType(), True),
    StructField("corp_code", StringType(), True),
    StructField("corp_name", StringType(), True),
    StructField("acqs_mth1", StringType(), True),
    StructField("acqs_mth2", StringType(), True),
    StructField("acqs_mth3", StringType(), True),
    StructField("stock_knd", StringType(), True),
    StructField("bsis_qy", StringType(), True),
    StructField("change_qy_acqs", StringType(), True),
    StructField("change_qy_dsps", StringType(), True),
    StructField("change_qy_incnr", StringType(), True),
    StructField("trmend_qy", StringType(), True),
    StructField("rm", StringType(), True)
])

major_shareholder = StructType([
    StructField("rcept_no", StringType(), True),
    StructField("corp_cls", StringType(), True),
    StructField("corp_code", StringType(), True),
    StructField("corp_name", StringType(), True),
    StructField("nm", StringType(), True),
    StructField("relate", StringType(), True),
    StructField("stock_knd", StringType(), True),
    StructField("bsis_posesn_stock_co", StringType(), True),
    StructField("bsis_posesn_stock_qota_rt", StringType(), True),
    StructField("trmend_posesn_stock_co", StringType(), True),
    StructField("trmend_posesn_stock_qota_rt", StringType(), True),
    StructField("rm", StringType(), True)
])

#최대주주 현황
major_share_chg = StructType([
    StructField("rcept_no", StringType(), True),  # 접수번호
    StructField("corp_cls", StringType(), True),  # 법인구분
    StructField("corp_code", StringType(), True),  # 고유번호
    StructField("corp_name", StringType(), True),  # 법인명
    StructField("nm", StringType(), True),  # 성명
    StructField("relate", StringType(), True),  # 관계
    StructField("stock_knd", StringType(), True),  # 주식 종류
    StructField("bsis_posesn_stock_co", StringType(), True),  # 기초 소유 주식 수
    StructField("bsis_posesn_stock_qota_rt", StringType(), True),  # 기초 소유 주식 지분 율
    StructField("trmend_posesn_stock_co", StringType(), True),  # 기말 소유 주식 수
    StructField("trmend_posesn_stock_qota_rt", StringType(), True),  # 기말 소유 주식 지분 율
    StructField("rm", StringType(), True)  # 비고
])

#소액주주 현황
minority_share = StructType([
    StructField("rcept_no", StringType(), True),  # 접수번호(14자리)
    StructField("corp_cls", StringType(), True),  # 법인구분: Y(유가), K(코스닥), N(코넥스), E(기타)
    StructField("corp_code", StringType(), True),  # 고유번호(8자리)
    StructField("corp_name", StringType(), True),  # 법인명
    StructField("se", StringType(), True),  # 구분: 소액주주
    StructField("shrholdr_co", StringType(), True),  # 주주수
    StructField("shrholdr_tot_co", StringType(), True),  # 전체 주주수
    StructField("shrholdr_rate", StringType(), True),  # 주주 비율
    StructField("hold_stock_co", StringType(), True),  # 보유 주식수
    StructField("stock_tot_co", StringType(), True),  # 총발행 주식수
    StructField("hold_stock_rate", StringType(), True),  # 보유 주식 비율
])

#임원 현황
exec_status = StructType([
    StructField("rcept_no", StringType(), True),  # 접수번호(14자리)
    StructField("corp_cls", StringType(), True),  # 법인구분: Y(유가), K(코스닥), N(코넥스), E(기타)
    StructField("corp_code", StringType(), True),  # 고유번호(8자리)
    StructField("corp_name", StringType(), True),  # 법인명
    StructField("nm", StringType(), True),  # 성명
    StructField("sexdstn", StringType(), True),  # 성별
    StructField("birth_ym", StringType(), True),  # 출생 년월: YYYY년 MM월
    StructField("ofcps", StringType(), True),  # 직위: 회장, 사장, 사외이사 등
    StructField("rgist_exctv_at", StringType(), True),  # 등기 임원 여부: 등기임원, 미등기임원 등
    StructField("fte_at", StringType(), True),  # 상근 여부: 상근, 비상근
    StructField("chrg_job", StringType(), True),  # 담당 업무: 대표이사, 이사, 사외이사 등
    StructField("main_career", StringType(), True),  # 주요 경력
    StructField("mxmm_shrholdr_relate", StringType(), True),  # 최대 주주 관계
    StructField("hffc_pd", StringType(), True),  # 재직 기간
    StructField("tenure_end_on", StringType(), True)  # 임기 만료 일
])

#직원 현황
emp_status = StructType([
    StructField("rcept_no", StringType(), True),  # 접수번호(14자리)
    StructField("corp_cls", StringType(), True),  # 법인구분: Y(유가), K(코스닥), N(코넥스), E(기타)
    StructField("corp_code", StringType(), True),  # 고유번호(8자리)
    StructField("corp_name", StringType(), True),  # 법인명
    StructField("fo_bbm", StringType(), True),  # 사업부문
    StructField("sexdstn", StringType(), True),  # 성별: 남, 여
    StructField("reform_bfe_emp_co_rgllbr", StringType(), True),  # 개정 전 직원 수 정규직
    StructField("reform_bfe_emp_co_cnttk", StringType(), True),  # 개정 전 직원 수 계약직
    StructField("reform_bfe_emp_co_etc", StringType(), True),  # 개정 전 직원 수 기타
    StructField("rgllbr_co", StringType(), True),  # 정규직 수
    StructField("rgllbr_abacpt_labrr_co", StringType(), True),  # 정규직 단시간 근로자 수
    StructField("cnttk_co", StringType(), True),  # 계약직 수
    StructField("cnttk_abacpt_labrr_co", StringType(), True),  # 계약직 단시간 근로자 수
    StructField("sm", StringType(), True),  # 합계
    StructField("avrg_cnwk_sdytrn", StringType(), True),  # 평균 근속 연수
    StructField("fyer_salary_totamt", StringType(), True),  # 연간 급여 총액
    StructField("jan_salary_am", StringType(), True),  # 1인평균 급여 액
    StructField("rm", StringType(), True)  # 비고
])

#이사·감사 개인별 보수 현황
indv_dir_aud_comp = StructType([
    StructField("rcept_no", StringType(), True),  # 접수번호(14자리)
    StructField("corp_cls", StringType(), True),  # 법인구분: Y(유가), K(코스닥), N(코넥스), E(기타)
    StructField("corp_code", StringType(), True),  # 고유번호(8자리)
    StructField("corp_name", StringType(), True),  # 법인명
    StructField("nm", StringType(), True),  # 이름
    StructField("ofcps", StringType(), True),  # 직위
    StructField("mendng_totamt", StringType(), True),  # 보수 총액
    StructField("mendng_totamt_ct_incls_mendng", StringType(), True)  # 보수 총액 비 포함 보수
])

#이사·감사 전체의 보수현황
all_dir_aud_comp = StructType([
    StructField("rcept_no", StringType(), True),  # 접수번호(14자리)
    StructField("corp_cls", StringType(), True),  # 법인구분: Y(유가), K(코스닥), N(코넥스), E(기타)
    StructField("corp_code", StringType(), True),  # 고유번호(8자리)
    StructField("corp_name", StringType(), True),  # 법인명
    StructField("nmpr", StringType(), True),  # 인원수
    StructField("mendng_totamt", StringType(), True),  # 보수 총액
    StructField("jan_avrg_mendng_am", StringType(), True),  # 1인 평균 보수 액
    StructField("rm", StringType(), True)  # 비고
])

#개인별 보수지급 금액(5억이상 상위5인)	
top5_exec_comp = StructType([
    StructField("rcept_no", StringType(), True),  # 접수번호(14자리)
    StructField("corp_cls", StringType(), True),  # 법인구분: Y(유가), K(코스닥), N(코넥스), E(기타)
    StructField("corp_code", StringType(), True),  # 고유번호(8자리)
    StructField("corp_name", StringType(), True),  # 법인명
    StructField("nm", StringType(), True),  # 이름
    StructField("ofcps", StringType(), True),  # 직위
    StructField("mendng_totamt", StringType(), True),  # 보수 총액
    StructField("mendng_totamt_ct_incls_mendng", StringType(), True)  # 보수 총액 비 포함 보수
])
#타법인 출자현황
other_corp_inv = StructType([
    StructField("rcept_no", StringType(), True),  # 접수번호(14자리)
    StructField("corp_cls", StringType(), True),  # 법인구분: Y(유가), K(코스닥), N(코넥스), E(기타)
    StructField("corp_code", StringType(), True),  # 고유번호(8자리)
    StructField("corp_name", StringType(), True),  # 회사명
    StructField("inv_prm", StringType(), True),  # 법인명
    StructField("frst_acqs_de", StringType(), True),  # 최초 취득 일자(YYYYMMDD)
    StructField("invstmnt_purps", StringType(), True),  # 출자 목적
    StructField("frst_acqs_amount", StringType(), True),  # 최초 취득 금액
    StructField("bsis_blce_qy", StringType(), True),  # 기초 잔액 수량
    StructField("bsis_blce_qota_rt", StringType(), True),  # 기초 잔액 지분 율
    StructField("bsis_blce_acntbk_amount", StringType(), True),  # 기초 잔액 장부 가액
    StructField("incrs_dcrs_acqs_dsps_qy", StringType(), True),  # 증가 감소 취득 처분 수량
    StructField("incrs_dcrs_acqs_dsps_amount", StringType(), True),  # 증가 감소 취득 처분 금액
    StructField("incrs_dcrs_evl_lstmn", StringType(), True),  # 증가 감소 평가 손액
    StructField("trmend_blce_qy", StringType(), True),  # 기말 잔액 수량
    StructField("trmend_blce_qota_rt", StringType(), True),  # 기말 잔액 지분 율
    StructField("trmend_blce_acntbk_amount", StringType(), True),  # 기말 잔액 장부 가액
    StructField("recent_bsns_year_fnnr_sttus_tot_assets", StringType(), True),  # 최근 사업 연도 재무 현황 총 자산
    StructField("recent_bsns_year_fnnr_sttus_thstrm_ntpf", StringType(), True)  # 최근 사업 연도 재무 현황 당기 순이익
])

#단일회사 주요 재무제표
single_corp_fin = StructType([
    StructField("bsns_year", StringType(), True),  # 사업 연도
    StructField("corp_code", StringType(), True),  # 고유번호(8자리)
    StructField("stock_code", StringType(), True),  # 종목 코드(6자리)
    StructField("reprt_code", StringType(), True),  # 보고서 코드
    StructField("idx_cl_code", StringType(), True),  # 지표분류코드
    StructField("idx_cl_nm", StringType(), True),  # 지표분류명
    StructField("idx_code", StringType(), True),  # 지표코드
    StructField("idx_nm", StringType(), True),  # 지표명
    StructField("idx_val", StringType(), True)  # 지표값
])

schema_set = {
    'cond_cap_sec_bal': ArrayType(cond_cap_sec_bal), 
    'exec_comp_stat': ArrayType(exec_comp_stat),
    'corp_bond_bal': ArrayType(corp_bond_bal),
    'short_bond_bal': ArrayType(short_bond_bal), 
    'com_paper_bal': ArrayType(com_paper_bal),
    'debt_sec_perf': ArrayType(debt_sec_perf), 
    #'priv_fund_use': ArrayType(priv_fund_use), 
     #'pub_fund_use': ArrayType(pub_fund_use), 
    'dir_aud_comp_gm': ArrayType(dir_aud_comp_gm), 
    'dir_aud_comp_type': ArrayType(dir_aud_comp_type), 
    'total_shares': ArrayType(total_shares), 
    #'auditor_name_op': ArrayType(auditor_name_op), 
    #'audit_serv_contr': ArrayType(audit_serv_contr), 
    'non_audit_contr': ArrayType(non_audit_contr), 
    'out_dir_stat': ArrayType(out_dir_stat), 
    'new_cap_sec_bal': ArrayType(new_cap_sec_bal), 
    'cap_inc_dec_stat': ArrayType(cap_inc_dec_stat), 
    'dividend_info': ArrayType(dividend_info), 
    'treasury_stock': ArrayType(treasury_stock), 
    'major_shareholder': ArrayType(major_shareholder), 
    'major_share_chg': ArrayType(major_share_chg), 
    'minority_share': ArrayType(minority_share), 
    'exec_status': ArrayType(exec_status), 
    'emp_status': ArrayType(emp_status), 
    'indv_dir_aud_comp': ArrayType(indv_dir_aud_comp), 
    'all_dir_aud_comp': ArrayType(all_dir_aud_comp), 
    'top5_exec_comp': ArrayType(top5_exec_comp), 
    'other_corp_inv': ArrayType(other_corp_inv), 
    'single_corp_fin': ArrayType(single_corp_fin)
    }