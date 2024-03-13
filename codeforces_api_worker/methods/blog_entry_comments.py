from codeforces_api_worker.request import request
from codeforces_api_worker.response_saver import save_response


def get_blog_entry_comments(blogEntryId:int):
    method_name = 'blogEntry.comments'
    
    response = request.request(method_name, locals())
    save_response(response, f'{method_name}_{blogEntryId}')