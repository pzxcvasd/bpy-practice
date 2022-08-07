def gen_centerpiece(context) :
  
  bpy.ops.mesh.primitive_cube_add(size=random.uniform(1,3))
  # 1~3 범위의 랜덤 사이즈대로 cube 를 추가한다. bpy.ops.mesh.primitive_cube_add 명령어 기억할 것
  
  cube = active_object()
  # 현재 선택된 오브젝트의 이름을 cube 라고 설정
  
  bpy.ops.object.modifier_add(type='WIREFRAME')
  #오브젝트에 와이어프레임 modifier 를 추가한다. (와이어프레임 -> 프레임만 있는 것)
  
  cube.modifiers["Wireframe"].thickness = random.uniform(0.03, 0.1)
  # 선택된 오브젝트 = cube 의 와이어프레임 modifier 의 굵기를 랜덤값으로 정한다.
