const temp = document.querySelector(".search-value");

console.log(temp.value);

function changeLoc() {
    const location = document.querySelector(".search").value;
    console.log("location: " + location);
    document.querySelector(".search-value").value = location;
    drawMap();
}

function drawMap() {
    console.log("drawMap() 실행");

  const mapContainer = document.getElementById("map"), // 지도를 표시할 div
    mapOption = {
      center: new kakao.maps.LatLng(37.482786, 127.045974), // 지도의 중심좌표
      level: 3, // 지도의 확대 레벨
    };

    // 지도를 생성합니다
    const map = new kakao.maps.Map(mapContainer, mapOption);

    const loc = document.querySelector(".search-value").value;

    const geocoder = new kakao.maps.services.Geocoder();

    // 주소로 좌표를 검색합니다
    geocoder.addressSearch(loc, function (result, status) {
        // 정상적으로 검색이 완료됐으면
        if (status === kakao.maps.services.Status.OK) {
            const coords = new kakao.maps.LatLng(result[0].y, result[0].x);

            // 결과값으로 받은 위치를 마커로 표시합니다
            const marker = new kakao.maps.Marker({
            map: map,
            position: coords,
            });
            
            // 여기서 axios로 해당 건물에 대한 model이 만들어있는지 확인하고, 없으면 만듦
            axios.post('/building/matching/', { 
                location: result[0].address_name,
                latitude: result[0].y,
                longitude: result[0].x })
            .then((response) => {
                console.log('요기');
                console.log(response);
                const infowindow = new kakao.maps.InfoWindow({
                    content:
                        `<div style="width:150px;text-align:center;padding:6px 0;"><a href="/building/${ response.data.bid }/">건물 정보 보기</a></div>`,
                        // 위에서 axios를 통해 만든(받아온) 건물 모델의 id를 이용해 해당 건물 정보 페이지로 보내줌.
                    });
                    infowindow.open(map, marker);
            })
            .catch((error) => console.error(error));


            // // 인포윈도우로 장소에 대한 설명을 표시합니다
            // const infowindow = new kakao.maps.InfoWindow({
            // content:
            //     '<div style="width:150px;text-align:center;padding:6px 0;"><a href=""></a></div>',
            //     // 위에서 axios를 통해 만든(받아온) 건물 모델의 id를 이용해 해당 건물 정보 페이지로 보내줌.
            // });
            // infowindow.open(map, marker);

            // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
            map.setCenter(coords);
    }
    // 오류 처리 해줘야 함!
    });
}

drawMap();


// <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
// <script>
//   const likeButton = document.getElementById("like-button");
//   const pickButton = document.getElementById("pick-button");
//   const likeCount = document.getElementById("like-count");
//   const postTitle = document.querySelector(".post_title");
//   const postContent = document.querySelector(".post_content");

//   const check = () => {
//     axios
//       .post("/checkLike", { post_pk: "{{post.pk}}" })
//       .then((res) => {
//         if (res.data.existing) {
//           likeButton.style.color = "red";
//         } else {
//           likeButton.style.color = "black";
//         } 
//       })
//       .catch((error) => console.error(error));

//     axios
//       .post("/checkPick", { post_pk: "{{post.pk}}" })
//       .then((res) => {
//         if (res.data.existing) {
//           postTitle.style.color = "blue";
//           postContent.style.color = "blue";
//           pickButton.style.color = "blue";
//         } else {
//           postTitle.style.color = "black";
//           postContent.style.color = "black";
//           pickButton.style.color = "black";
//         }
//       })
//       .catch((error) => console.error(error));
//   };

//   const like = () => {
//     axios
//       .post("/like", { post_pk: "{{post.pk}}" })
//       .then((res) => {
//         if (res.data.check) {
//           likeButton.style.color = "red";
//         } else {
//           likeButton.style.color = "black";
//         }
//         likeCount.innerHTML = "좋아요 " + res.data.like_count + " 개";
//       })
//       .catch((error) => console.error(error));
//   };

//   const pick = () => {
//     axios
//       .post("/pick", { post_pk: "{{post.pk}}" })
//       .then((res) => {
//         if (res.data.check) {
//           postTitle.style.color = "blue";
//           postContent.style.color = "blue";
//           pickButton.style.color = "blue";
//         } else {
//           postTitle.style.color = "black";
//           postContent.style.color = "black";
//           pickButton.style.color = "black";
//         }
//       })
//       .catch((error) => console.error(error));
//   };

//   function init() {
//     check();
//   }
//   init();
// </script>
