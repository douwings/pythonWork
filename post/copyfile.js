let OSS = require('ali-oss');

let client = new OSS({
    region: 'oss-cn-hangzhou',
    accessKeyId: 'accessKeyId',
    accessKeySecret: 'accessKeySecret',
    bucket: 'zymediapr',
});



async function copy () {
  try {
     // 两个Bucket之间拷贝
    let result = await client.copy('compress_test/big_buck_bunny.mp4', '/zymediao/compress_test/big_buck_bunny.mp4');
    console.log(result);

    // // 拷贝元信息
    // let result = await client.copy('/compress_test/big_buck_bunny.mp4', '/zymediao/compress_test/big_buck_bunny.mp4');
    // console.log(result);

    // // 覆盖元信息
    // let result = await client.copy('/compress_test/big_buck_bunny.mp4', '/zymediao/compress_test/big_buck_bunny.mp4');
    // console.log(result);
  } catch (e) {
    console.log(e);
  }
}

copy()
