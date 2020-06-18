# -*- coding: utf-8 -*-
import oss2


# # get
# # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
# auth = auth = oss2.Auth('LTAIktjTb9MWQ1lc', 'OQToVyBnH32bnUpSFLSvbVbhqdMryC')
# # Endpoint以杭州为例，其它Region请按实际情况填写。
# # bucket = oss2.Bucket(auth, 'http://oss-cn-shenzhen.aliyuncs.com', 'zhiyundata')
# bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'zymediao')

# # 获取文件的部分元信息
# simplifiedmeta = bucket.get_object_meta('kmstest/5S3lab.mp4')
# print(simplifiedmeta.headers['Last-Modified']) 
# print(simplifiedmeta.headers['Content-Length']) 
# print(simplifiedmeta.headers['ETag']) 

# # 获取文件的全部元信息
# objectmeta = bucket.head_object('kmstest/5S3lab.mp4')
# print(objectmeta.headers['Content-Type']) 
# print(objectmeta.headers['Last-Modified']) 
# print(objectmeta.headers['x-oss-object-type'])



# list
# 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
auth = oss2.Auth('LTAIktjTb9MWQ1lc', 'OQToVyBnH32bnUpSFLSvbVbhqdMryC')
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-shenzhen.aliyuncs.com', 'zhiyundata')
# bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'zymediapr')

# 列举包含指定前缀的文件。默认列举100个文件。
for obj in oss2.ObjectIterator(bucket,prefix = ''):  #afterMts  kmstest
    print(obj.key)



# copy
# # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
# auth = oss2.Auth('LTAIktjTb9MWQ1lc', 'OQToVyBnH32bnUpSFLSvbVbhqdMryC')
# # Endpoint以杭州为例，其它Region请按实际情况填写。
# bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'zymediapr')

# bucket.copy_object('zymediao', 'compress_test/big_buck_bunny.mp4', 'compress_test/big_buck_bunny.mp4')


# # delete
# # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
# auth = oss2.Auth('LTAIktjTb9MWQ1lc', 'OQToVyBnH32bnUpSFLSvbVbhqdMryC')
# # Endpoint以杭州为例，其它Region请按实际情况填写。
# bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'zymediapr')
# # bucket = oss2.Bucket(auth, 'http://oss-cn-shenzhen.aliyuncs.com', 'zhiyundata')

# bucket.delete_object('afterMts/0130120933C5EF3561D4A87D7C3C1B43-2_01.mp4')   #afterMts/0130120933C5EF3561D4A87D7C3C1B43-2_01.mp4    kmstest/5S3labx.mp4