import braintree
from braintree.resource import Resource
from braintree.settlement_batch_summary import SettlementBatchSummary
from braintree.successful_result import SuccessfulResult
from braintree.error_result import ErrorResult

class SettlementBatchSummaryGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def generate(self, settlement_date):
        response = self.config.http().post('/settlement_batch_summary', { "settlement_batch_summary": { "settlement_date": settlement_date}})
        if "settlement_batch_summary" in response:
            return SuccessfulResult({"settlement_batch_summary": SettlementBatchSummary(self.gateway, response["settlement_batch_summary"])})
        elif "api_error_response" in response:
            return ErrorResult(self.gateway, response["api_error_response"])