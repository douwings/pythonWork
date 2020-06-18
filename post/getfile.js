let OSS = require('ali-oss');

async function getFile(region, bucket, inputObject, getname) {
    let client = new OSS({
        region: region,
        accessKeyId: 'LTAIktjTb9MWQ1lc',
        accessKeySecret: 'OQToVyBnH32bnUpSFLSvbVbhqdMryC',
        bucket: bucket,
    });
    try {
        let result = await client.get(inputObject, getname);
        console.log(result)
        if (result.status != 200) {
            return result.content
        } else {
            return false
        }

    } catch (e) {
        console.log("getfailerror",e)
        return false
    }
}

var firstdownloadregion = 'oss-cn-hangzhou'
var firstdownloadbucket = 'zymediapr'
var inputObject = 'afterMts/0130120933C5EF3561D4A87D7C3C1B43-2_01.mp4'
var filepath = 'F:/afterMts/0130120933C5EF3561D4A87D7C3C1B43-2_01.mp4'

getFile(firstdownloadregion, firstdownloadbucket, inputObject, filepath)
