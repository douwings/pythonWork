import json
from aliyunsdkmts.request.v20140618 import SearchPipelineRequest
from aliyunsdkcore import client
region = 'cn-hangzhou'
access_key_id = 'LTAIktjTb9MWQ1lc'
access_key_secret = 'OQToVyBnH32bnUpSFLSvbVbhqdMryC'
client = client.AcsClient(access_key_id, access_key_secret, region)
request = SearchPipelineRequest.SearchPipelineRequest()
response = client.do_action_with_exception(request);
json_response = json.loads(response)
pipelines = json_response['PipelineList']['Pipeline']
for pipeline in pipelines:
    print ('pipeline id:' + pipeline['Id'] + ', name:' + pipeline['Name'] + ', state:' + pipeline['State'])