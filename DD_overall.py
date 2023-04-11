# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 21:14:25 2022

@author: simpleU
"""

import re
import json
import requests
from bs4 import BeautifulSoup
from gazpacho import Soup
import pandas as pd

def DD(ticker):
    try:
        url = f'https://roic.ai/financials/{ticker}?fs=annual'
        soup = Soup.get(url)
        scrapped_data = soup.find('script', {'id': "__NEXT_DATA__"})
        data = json.loads(scrapped_data.text)
    #### balance_sheet

        BS_quart = pd.DataFrame(data["props"]["pageProps"]["data"]["data"]["bsq"])
        BS_quart=BS_quart[['date','symbol','cik','cashAndCashEquivalents','shortTermInvestments','cashAndShortTermInvestments','otherCurrentAssets',\
        'totalCurrentAssets','longTermInvestments','otherAssets','totalAssets','accountPayables','shortTermDebt','taxPayables','otherCurrentLiabilities',\
        'totalCurrentLiabilities','longTermDebt','deferredRevenueNonCurrent','deferredTaxLiabilitiesNonCurrent','totalLiabilities','preferredStock',\
        'commonStock','retainedEarnings','accumulatedOtherComprehensiveIncomeLoss','minorityInterest','totalEquity','totalLiabilitiesAndTotalEquity',\
        'totalInvestments','totalDebt','netDebt']]
        scale=1000000000
        BS_quart['cashAndCashEquivalents']=BS_quart['cashAndCashEquivalents']/scale
        BS_quart['shortTermInvestments']=BS_quart['shortTermInvestments']/scale
        BS_quart['cashAndShortTermInvestments']=BS_quart['cashAndShortTermInvestments']/scale
        BS_quart['otherCurrentAssets']=BS_quart['otherCurrentAssets']/scale
        BS_quart['totalCurrentAssets']=BS_quart['totalCurrentAssets']/scale
        BS_quart['longTermInvestments']=BS_quart['longTermInvestments']/scale
        BS_quart['otherAssets']=BS_quart['otherAssets']/scale
        BS_quart['totalAssets']=BS_quart['totalAssets']/scale
        BS_quart['accountPayables']=BS_quart['accountPayables']/scale
        BS_quart['shortTermDebt']=BS_quart['shortTermDebt']/scale
        BS_quart['taxPayables']=BS_quart['taxPayables']/scale
        BS_quart['otherCurrentLiabilities']=BS_quart['otherCurrentLiabilities']/scale
        BS_quart['totalCurrentLiabilities']=BS_quart['totalCurrentLiabilities']/scale
        BS_quart['longTermDebt']=BS_quart['longTermDebt']/scale
        BS_quart['deferredRevenueNonCurrent']=BS_quart['deferredRevenueNonCurrent']/scale
        BS_quart['deferredTaxLiabilitiesNonCurrent']=BS_quart['deferredTaxLiabilitiesNonCurrent']/scale
        BS_quart['totalLiabilities']=BS_quart['totalLiabilities']/scale
        BS_quart['preferredStock']=BS_quart['preferredStock']/scale
        BS_quart['commonStock']=BS_quart['commonStock']/scale
        BS_quart['retainedEarnings']=BS_quart['retainedEarnings']/scale
        BS_quart['accumulatedOtherComprehensiveIncomeLoss']=BS_quart['accumulatedOtherComprehensiveIncomeLoss']/scale
        BS_quart['minorityInterest']=BS_quart['minorityInterest']/scale
        BS_quart['totalEquity']=BS_quart['totalEquity']/scale
        BS_quart['totalLiabilitiesAndTotalEquity']=BS_quart['totalLiabilitiesAndTotalEquity']/scale
        BS_quart['totalInvestments']=BS_quart['totalInvestments']/scale
        BS_quart['totalDebt']=BS_quart['totalDebt']/scale
        BS_quart['netDebt']=BS_quart['netDebt']/scale
        ###### Income sheet
        IS_quart = pd.DataFrame(data["props"]["pageProps"]["data"]["data"]["isq"])
        IS_quart =IS_quart[['date','symbol','cik','revenue','costOfRevenue','grossProfit','grossProfitRatio','researchAndDevelopmentExpenses',\
                        'generalAndAdministrativeExpenses','sellingAndMarketingExpenses','sellingGeneralAndAdministrativeExpenses','otherExpenses',\
                        'operatingExpenses','costAndExpenses','interestIncome','interestExpense','depreciationAndAmortization','ebitda','ebitdaratio',\
                        'operatingIncome','operatingIncomeRatio','totalOtherIncomeExpensesNet','netIncome','eps','epsdiluted','weightedAverageShsOut',\
                        'weightedAverageShsOutDil','link','finalLink']]
        IS_quart['revenue']=IS_quart['revenue']/scale
        IS_quart['costOfRevenue']=IS_quart['costOfRevenue']/scale
        IS_quart['grossProfit']=IS_quart['grossProfit']/scale
        IS_quart['grossProfitRatio']=IS_quart['grossProfitRatio']/scale
        IS_quart['researchAndDevelopmentExpenses']=IS_quart['researchAndDevelopmentExpenses']/scale
        IS_quart['generalAndAdministrativeExpenses']=IS_quart['generalAndAdministrativeExpenses']/scale
        IS_quart['sellingAndMarketingExpenses']=IS_quart['sellingAndMarketingExpenses']/scale
        IS_quart['sellingGeneralAndAdministrativeExpenses']=IS_quart['sellingGeneralAndAdministrativeExpenses']/scale
        IS_quart['otherExpenses']=IS_quart['otherExpenses']/scale
        IS_quart['operatingExpenses']=IS_quart['operatingExpenses']/scale
        IS_quart['costAndExpenses']=IS_quart['costAndExpenses']/scale
        IS_quart['interestIncome']=IS_quart['interestIncome']/scale
        IS_quart['interestExpense']=IS_quart['interestExpense']/scale
        IS_quart['depreciationAndAmortization']=IS_quart['depreciationAndAmortization']/scale
        IS_quart['ebitda']=IS_quart['ebitda']/scale
        IS_quart['ebitdaratio']=IS_quart['ebitdaratio']/scale
        IS_quart['operatingIncome']=IS_quart['operatingIncome']/scale
        IS_quart['operatingIncomeRatio']=IS_quart['operatingIncomeRatio']/scale
        IS_quart['totalOtherIncomeExpensesNet']=IS_quart['totalOtherIncomeExpensesNet']/scale
        IS_quart['netIncome']=IS_quart['netIncome']/scale
        IS_quart['eps']=IS_quart['eps']
        IS_quart['epsdiluted']=IS_quart['epsdiluted']
        IS_quart['weightedAverageShsOut']=IS_quart['weightedAverageShsOut']/scale
        IS_quart['weightedAverageShsOutDil']=IS_quart['weightedAverageShsOutDil']/scale
        ##### Cash sheet
        cs_quart = pd.DataFrame(data["props"]["pageProps"]["data"]["data"]["cfq"])
        cs_quart = cs_quart[['date','symbol','cik','netIncome','depreciationAndAmortization','stockBasedCompensation','changeInWorkingCapital',\
                             'acquisitionsNet','purchasesOfInvestments','salesMaturitiesOfInvestments','netCashUsedForInvestingActivites','debtRepayment','commonStockIssued',\
                            'commonStockRepurchased','dividendsPaid','netCashUsedProvidedByFinancingActivities','netChangeInCash','operatingCashFlow','capitalExpenditure',\
                            'freeCashFlow','link','finalLink']]
        cs_quart['netIncome']=cs_quart['netIncome']/scale
        cs_quart['depreciationAndAmortization']=cs_quart['depreciationAndAmortization']/scale
        cs_quart['stockBasedCompensation']=cs_quart['stockBasedCompensation']/scale
        cs_quart['changeInWorkingCapital']=cs_quart['changeInWorkingCapital']/scale
        cs_quart['acquisitionsNet']=cs_quart['acquisitionsNet']/scale
        cs_quart['purchasesOfInvestments']=cs_quart['purchasesOfInvestments']/scale
        cs_quart['salesMaturitiesOfInvestments']=cs_quart['salesMaturitiesOfInvestments']/scale
        cs_quart['netCashUsedForInvestingActivites']=cs_quart['netCashUsedForInvestingActivites']/scale
        cs_quart['debtRepayment']=cs_quart['debtRepayment']/scale
        cs_quart['commonStockIssued']=cs_quart['commonStockIssued']/scale
        cs_quart['commonStockRepurchased']=cs_quart['commonStockRepurchased']/scale
        cs_quart['dividendsPaid']=cs_quart['dividendsPaid']/scale
        cs_quart['netCashUsedProvidedByFinancingActivities']=cs_quart['netCashUsedProvidedByFinancingActivities']/scale
        cs_quart['netChangeInCash']=cs_quart['netChangeInCash']/scale
        cs_quart['operatingCashFlow']=cs_quart['operatingCashFlow']/scale
        cs_quart['capitalExpenditure']=cs_quart['capitalExpenditure']/scale
        cs_quart['freeCashFlow']=cs_quart['freeCashFlow']/scale
        ###### outlook
        outlk = pd.DataFrame(data["props"]["pageProps"]["data"]["data"]["outlook"])
        #outlk=outlk[['profile',
        #metrics
        #financialsAnnual
        #financialsQuarter
        #fslink
        #insideTrades
        #splitHistory
        #stockDividend
        #stockNews
        #rating
        
        
        #    for col in outlk.columns:
        #        print(col)
        overall = pd.concat([cs_quart['date'],cs_quart['symbol'],cs_quart['freeCashFlow'], cs_quart['netChangeInCash'],BS_quart['preferredStock'],\
            BS_quart['totalDebt'],IS_quart['revenue'],IS_quart['grossProfit'],IS_quart['ebitda'],IS_quart['eps'],cs_quart['netIncome'],cs_quart['commonStockRepurchased'],\
            cs_quart['dividendsPaid'],], axis=1)
        return overall
    
    except:
        dum=-9999
        dummy=pd.DataFrame({'date':[dum],'symbol':[dum],'freeCashFlow':[dum],'netChangeInCash':[dum],'preferredStock':[dum],'revenue':[dum],'totalDebt':[dum],'grossProfit':[dum],'ebitda':[dum],'eps':[dum],'netIncome':[dum],'dividendsPaid':[dum],'commonStockRepurchased':[dum]})
        return dummy
    ###### Summary Score
    # make debt negative
    # get running average and direction for each score
    # sum up each column together running average 
    # send back stock score and price
