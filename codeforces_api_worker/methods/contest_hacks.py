from codeforces_api_worker.request import request
from codeforces_api_worker.response_saver import save_response


def get_constest_hacks(contestId:int, asManager:bool=None):
    method_name = 'contest.hacks'

    response = request.request(method_name, locals())
    save_response(response, f'{method_name}_{contestId}')