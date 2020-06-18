# -*- coding: utf8 -*-
import json
import time
from urllib.parse import quote
from aliyunsdkcore.client import AcsClient
from aliyunsdkmts.request.v20140618 import QueryJobListRequest
access_key_id = 'LTAIktjTb9MWQ1lc'
access_key_secret = 'OQToVyBnH32bnUpSFLSvbVbhqdMryC'
mps_region_id = 'cn-hangzhou'

pipeline_id = '9dbb121b4935480f859022c350d3194d'

job_id = '3f441ca2dc6a41f28562744e28ee8f99'

oss_bucket = 'zymediapr'

def queryjoblist(job_id):
    while True:
        # 创建AcsClient实例
        client = AcsClient(access_key_id, access_key_secret, mps_region_id)
        # 创建request，并设置参数
        request = QueryJobListRequest.QueryJobListRequest()
        request.set_accept_format('json')
        # JobId
        request.set_JobIds(job_id)

        # 发起API请求并显示返回值
        response_str = client.do_action_with_exception(request)
        response = json.loads(response_str)
        # print("response",response['JobList']['Job'])
        if response['JobList']['Job'][0]['State'] == 'TranscodeSuccess' :
            print("Success")
            return 'Success'
        elif response['JobList']['Job'][0]['State'] == 'TranscodeFail' :
            return 'Fail'
        elif response['JobList']['Job'][0]['State'] == 'Transcoding':
            print('wait')
            time.sleep(1)


if __name__ == '__main__':
    queryjoblist(job_id)