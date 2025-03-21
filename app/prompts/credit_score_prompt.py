def credit_score_prompt_maker(bank_summary,ais_summary,bureau_data):
    prompt = f""" 
You are an expert credit risk analyst. Analyze the applicant's financial health and creditworthiness based on the following data sources:

1. Annual Information Statement (AIS) Summary
2. Bank Statement Summary
3. Multi-Bureau Aggregated API Data (excluding the normalized credit score)

Your task:
- Evaluate the applicant’s credit risk
- Recommend a loan approval decision (Approve / Decline / Approve with Conditions)
- Suggest appropriate lending terms (Loan amount, interest rate, tenure)
- Provide risk mitigation strategies, if required

---

Data Inputs:

AIS Summary:
- Total Interest Income (Savings + Term Deposits): ₹[ENTER HERE]
- Mutual Fund Sale Proceeds: ₹[ENTER HERE]
- Other Income Reported: ₹[ENTER HERE]
- Tax Paid / Refund Status: ₹[ENTER HERE]
- PAN Verified: [Yes/No]

Bank Statement Summary:
- Average Monthly Balance: ₹[ENTER HERE]
- Total Credits in Last 6 Months: ₹[ENTER HERE]
- Total Debits in Last 6 Months: ₹[ENTER HERE]
- Loan EMIs Paid: ₹[ENTER HERE]
- Overdraft / Negative Balances: [Yes/No]
- Cheque Bounce Instances: [ENTER NUMBER]
- Cash Flow Trend: [Stable/Volatile]

Multi-Bureau API Data (other than normalized credit score):
{
  "status": "success",
  "message": {
    "USERNAME": "[ENTER NAME]",
    "CREDIT_SCORE": [ENTER SCORE],
    "CURRENT_LOANS": [
      {
        "AMOUNT": [ENTER AMOUNT],
        "BANK": "[ENTER BANK]",
        "TIME_PERIOD": "[ENTER TIME PERIOD]"
      }
    ],
    "NO_OF_TIMES_DEFAULTED": {
      "[ENTER BANK]": [ENTER COUNT]
    },
    "SETTLED_LOANS": [
      {
        "AMOUNT": [ENTER AMOUNT],
        "BANK": "[ENTER BANK]",
        "TIME_PERIOD": "[ENTER TIME PERIOD]"
      }
    ],
    "MISSED_PAYMENTS": {
      "[ENTER BANK]": [ENTER COUNT]
    }
  }
}

---

Output Instructions:
Provide a comprehensive recommendation report, including:

1. Applicant Profile Summary
2. Creditworthiness Assessment
3. Identified Risks
4. Final Lending Decision: Approve / Decline / Approve with Conditions
5. Justification for the Decision
6. Recommended Lending Terms:
   - Maximum Loan Amount
   - Interest Rate Range
   - Tenure
   - Collateral Requirement
7. Risk Mitigation Suggestions

only provide a json data no other text than json data

here is the bank statement summary:-
{bank_summary}

here is the ais summary:-
{ais_summary}


here is the Bureau data:-
{bureau_data}

"""