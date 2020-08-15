function whereami(elt, elt2) {
  var options = {
    enableHighAccuracy: false,
    maximumAge: 30000,
    timeout: 15000,
  };

  if (navigator.geolocation)
    navigator.geolocation.getCurrentPosition(success, error, options);
  else elt.innerHTML = "이 브라우저에서는 Geolocation이 지원되지 않습니다.";

  function error(e) {
    elt.innerHTML = "Geolocation 오류 " + e.code + ": " + e.message;
  }
  // geolocation 요청이 성공하면 이 함수가 호출된다.
  function success(pos) {
    var locs = {
      안암역: [37.586252, 127.028997],
      개운사: [37.589183, 127.028482],
      정후: [37.586891, 127.0301],
      법후: [37.592213, 127.034908],
    };
    var arr = {};
    var msg = [pos.coords.latitude, pos.coords.longitude];
    for (var key in locs) {
      var abs =
        Math.abs(locs[key][0] - msg[0]) + Math.abs(locs[key][1] - msg[1]);
      arr[key] = abs;
    }
    console.log(arr);
    arr = Object.keys(arr).sort(function (a, b) {
      return arr[a] - arr[b];
    });
    console.log(arr);
    elt.value = arr[0];
    elt2.value = msg;
  }
}
