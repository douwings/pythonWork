//方法一：
var url = "/dict/test";
var params = {advertiserUid: 1232131, advertiserWeiboNickname: "18"};
var xhr = new XMLHttpRequest();
xhr.open("POST", url, true);
xhr.setRequestHeader("Content-Type", "application/json");
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
xhr.send(JSON.stringify(params));

//方法二：
var url = "/dict/test";
var params = "score=5&abc=6";
var xhr = new XMLHttpRequest();
xhr.open("POST", url, true);
xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded"); 
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
xhr.send(params);



var url = "/dict/test";
var params = {advertiserUid: 1232131, advertiserWeiboNickname: "18"};
var xhr = new XMLHttpRequest();
xhr.open("POST", url, true);
xhr.setRequestHeader("Content-Type", "application/json");
xhr.onload = function (e) {
    console.log(xhr.responseText);
};
xhr.send(JSON.stringify(params));