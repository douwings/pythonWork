var url = "https://api.zhiyun-tech.com/v1/share/post/recommend?page=1&pageSize=30&token=6950d49125280beb825e3b5c9269b195&lang=ZH_CN";
var xhr = new XMLHttpRequest();
xhr.open("GET", url, true);
xhr.onload = function (e) {
  if (xhr.readyState === 4) {
    if (xhr.status === 200) {
      console.log(xhr.responseText);
    } else {
      console.error(xhr.statusText);
    }
  }
};
xhr.onerror = function (e) {
  console.error(xhr.statusText);
};
xhr.send(null);



var url = "https://api.zhiyun-tech.com/v1/share/post/recommend?page=1&pageSize=30&token=6950d49125280beb825e3b5c9269b195&lang=ZH_CN";
var xhr = new XMLHttpRequest();
xhr.open("GET", url, true);
xhr.onload = function (e) {
    console.log(xhr.responseText);
  };
xhr.send();