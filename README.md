# bpy-practice

## 1. cube_moving

큐브가 움직이는 애니메이션을 구현한 블렌더 파이썬 코드

## 2. Wireframe Cube Loop
와이어프레임 큐브의 애니메이션을 구현한 블렌더 파이썬 코드 분석 <br>
( 참조 : https://youtu.be/3rNqVPtbhzc?t=149 )

### 2-1. cube_add.py
* 랜덤값에 따른 wireframe 형 cube 구현
<div style="display: flex;">
  <img width="30%" alt="스크린샷 2022-08-08 00 32 18" src="https://user-images.githubusercontent.com/99024754/183298744-992a3d54-1de4-424c-904e-0d159fd56e26.png">
  <img width="30%" alt="스크린샷 2022-08-08 00 32 03" src="https://user-images.githubusercontent.com/99024754/183298748-2fd0bb58-9c35-4fb8-acfe-86b64213da4d.png">
  <img width="30%" alt="스크린샷 2022-08-08 00 31 59" src="https://user-images.githubusercontent.com/99024754/183298751-d6dee5ea-d52b-4b03-8f5b-9d65a239d300.png">
  </div>

`gen_centerpiece` 라는 함수를 통해 cube 를 추가하고, 추가된 큐브에 modifier 를 적용시켜서 큐브가 wireframe 형으로 나오게끔 구현하였다.<br>
또한 추가되는 cube 의 사이즈와 wireframe thickness 를 랜덤으로 적용하기 위해 random 값을 받게끔 구현하였다.



