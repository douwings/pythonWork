# -*- coding: utf8 -*-
import json
from urllib.parse import quote
from aliyunsdkcore.client import AcsClient
from aliyunsdkmts.request.v20140618 import SubmitJobsRequest
import queryjoblist
access_key_id = 'LTAIktjTb9MWQ1lc'
access_key_secret = 'OQToVyBnH32bnUpSFLSvbVbhqdMryC'
mps_region_id = 'cn-hangzhou'
pipeline_id = '53a85fb71e3e417ea15c7c0e583a823f'
# pipeline_id = '7cbdc75b801e42d6800317fcd903e406'
template_id = 'S00000003-200050'
# template_id = 'S00000001-200010'
oss_location = 'oss-cn-hangzhou'
# oss_bucket = 'kmstest'
oss_bucket = 'zymediao'
oss_output_bucket = 'zymediapr'

oss_input_object = 'compress_test/big_buck_bunny.mp4'
oss_output_object = 'compress_test/big_buck_bunny_mts.mp4'


def alimts(oss_input_object,oss_output_object):
    # 创建AcsClient实例
    client = AcsClient(access_key_id, access_key_secret, mps_region_id)
    # 创建request，并设置参数
    request = SubmitJobsRequest.SubmitJobsRequest()
    request.set_accept_format('json')
    # Input
    job_input = {'Location': oss_location,
                'Bucket': oss_bucket,
                 'Object': quote(oss_input_object) }
    request.set_Input(json.dumps(job_input))
    # Output
    output = {'OutputObject': quote(oss_output_object)}
    # Ouput->Container
    output['Container'] = {'Format': 'mp4'}
    # Ouput->Video
    output['Video'] = {'Codec': 'H.264',
                       'Bitrate': 1500,
                       'Width': 1280,
                       'Fps': 25}
    # Ouput->Audio
    output['Audio'] = {'Codec': 'AAC',
                       'Bitrate': 128,
                       'Channels': 2,
                       'Samplerate': 44100}
    # Ouput->TemplateId
    output['TemplateId'] = template_id
    outputs = [output]
    request.set_Outputs(json.dumps(outputs))
    request.set_OutputBucket(oss_output_bucket)
    request.set_OutputLocation(oss_location)
    # PipelineId
    request.set_PipelineId(pipeline_id)
    print("get_PipelineId",request.get_PipelineId())
    # 发起API请求并显示返回值
    response_str = client.do_action_with_exception(request)
    response = json.loads(response_str)
    if response['JobResultList']['JobResult'][0]['Success']:
        print ('JobId is:', response['JobResultList']['JobResult'][0]['Job']['JobId'])
        JobId = response['JobResultList']['JobResult'][0]['Job']['JobId']
        queryjoblist.queryjoblist(JobId)
    else:
        print ('SubmitJobs Failed code:',
               response['JobResultList']['JobResult'][0]['Code'],
               ' message:',
               response['JobResultList']['JobResult'][0]['Message'])
        result = str(response['JobResultList']['JobResult'][0]['Code']) + "   " +str(response['JobResultList']['JobResult'][0]['Message'])
        return result


if __name__ == '__main__':
    alimts(oss_input_object,oss_output_object)