<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<link href='http://fonts.googleapis.com/css?family=Open+Sans:400,300,700' rel='stylesheet' type='text/css'>

	<link rel="stylesheet" href="css/reset.css"> <!-- CSS reset -->
	<link rel="stylesheet" href="css/style.css"> <!-- Resource style -->
	<script src="js/modernizr.js"></script> <!-- Modernizr -->
  	
	<title>My Twinkles</title>
</head>
<body>
	<form class="cd-form floating-labels" action = "Result.jsp">
		<fieldset>
			<legend>반짝이 검색 서비스 HoxyNado</legend>

			<div class="error-message">
				<p>"나에게도 누군가 대쉬해올거라는 그 안일한 생각!" - 아이작 뉴턴</p>
			</div>

			<div class="icon">
				<label class="cd-label" for="cd-name">이름 초성</label>
				<input class="user" type="text" name="cd-name" id="cd-name" maxlength="3" required>
		    </div> 
            
            <div>
				<h4>성별</h4>

				<ul class="cd-form-list">
					<li>
						<input type="radio" name="radio-button" id="cd-radio-1" checked value="M">
						<label for="cd-radio-1">남자</label>
					</li>
						
					<li>
						<input type="radio" name="radio-button" id="cd-radio-2" value="F">
						<label for="cd-radio-2">여자</label>
					</li>
				</ul>
			</div>

		    <div class="icon">
		    	<label class="cd-label" for="cd-company">학번 (두자리로 입력하세요!)</label>
				<input class="company" type="text" name="cd-year" id="cd-year" pattern="[0-9][0-9]" maxlength="2" required>
		    </div> 
            
            <div>
				<h4>학과</h4>

				<p class="cd-select icon">
					<select id="major" name="major">
						<option value="0" selected>학과를 선택해주세요.</option>
						<option value="간호학과">간호학과</option>
                        <option value="건축공학과">건축공학과</option>
                        <option value="건축학과">건축학과</option>
                        <option value="도시공학과">도시공학과</option>
                        <option value="토목공학과">토목공학과</option>
                        <option value="건설융합학부">건설융합학부</option>
                        <option value="경영학과">경영학과</option>
                        <option value="경제학부">경제학부</option>
                        <option value="고고학과">고고학과</option>
                        <option value="고분자공학과">고분자공학과</option>
                        <option value="공공정책학부">공공정책학부</option>
                        <option value="관광컨벤션학과">관광컨벤션학과</option>
                        <option value="광메카트로닉스공학과">광메카트로닉스공학과</option>
                        <option value="국어교육과">국어교육과</option>
                        <option value="국어국문학과">국어국문학과</option>
                        <option value="국제학부">국제학부</option>
                        <option value="기계공학과">기계공학과</option>
                        <option value="나노메카트로닉스공학과">나노메카트로닉스공학과</option>
                        <option value="나노에너지공학과">나노에너지공학과</option>
                        <option value="노어노문학과">노어노문학과</option>
                        <option value="대기환경과학과">대기환경과학과</option>
                        <option value="도시공학과">도시공학과</option>
                        <option value="독어교육">독어교육과</option>
                        <option value="독어독문학과">독어독문학과</option>
                        <option value=">동물생명자원과학과">동물생명자원과학과</option>
                        <option value="디자인학과">디자인학과</option>
                        <option value="무역학부">무역학부</option>
                        <option value="무용학과">무용학과</option>
                        <option value="문헌정보학과">문헌정보학과</option>
                        <option value="물리교육과">물리교육과</option>
                        <option value="물리학과">물리학과</option>
                        <option value="미생물학">미생물학과</option>
                        <option value="미술학과">미술학과</option>
                        <option value="바이오산업기계공학과">바이오산업기계공학과</option>
                        <option value="바이오소재과학과">바이오소재과학과</option>
                        <option value="바이오환경에너지학과">바이오환경에너지학과</option> 
                        <option value="분자생물학과">분자생물학과</option>
                        <option value="불어교육과">불어교육과</option>
                        <option value="불어불문학과">불어불문학과</option>
                        <option value="사학과">사학과</option>
                        <option value="사회복지학과">사회복지학과</option>
                        <option value="사회학과">사회학과</option>
                        <option value="산업공학과">산업공학과</option>
                        <option value="생명과학과">생명과학과</option>
                        <option value="생명환경화학과">생명환경화학과</option>
                        <option value="생물교육과">생물교육과</option>
                        <option value="수학과">수학과</option>
                        <option value="수학교육과">수학교육과</option>
                        <option value="스포츠과학부">스포츠과학부</option>
                        <option value="식물생명과학과">식물생명과학과</option>
                        <option value="식품공학과">식품공학과</option>
                        <option value="식품영양학과">식품영양학과</option>
                        <option value="신문방송학과">신문방송학과</option>
                        <option value="실내환경디자인학과">실내환경디자인학과</option>
                        <option value="심리학과">심리학과</option>
                        <option value="아동가족학과">아동가족학과</option>
                        <option value="약학부">약학부</option>
                        <option value="언어정보학과">언어정보학과</option>
                        <option value="역사교육과">역사교육과</option>
                        <option value="영어교육과">영어교육과</option>
                        <option value="영어영문학과">영어영문학과</option>
                        <option value="예술문화영상학과">예술문화영상학과</option>
                        <option value="원예생명과학과">원예생명과학과</option>
                        <option value="유기소재시스템공학과">유기소재시스템공학과</option>
                        <option value="유아교육과">유아교육과</option>
                        <option value="윤리교육과">윤리교육과</option>
                        <option value="음악학과">음악학과</option>
                        <option value="유기소재시스템공학과">유기소재시스템공학과</option>
                        <option value="의류학과">의류학과</option>
                        <option value="의예과">의예과</option>
                        <option value="의학과">의학과</option>
                        <option value="일반사회교육과">일반사회교육과</option>
                        <option value="일어일문학과">일어일문학과</option>
                        <option value="재료공학부">재료공학부</option>
                        <option value="전기공학과">전기공학과</option>
                        <option value="전기컴퓨터공학부">전기컴퓨터공학부</option>
                        <option value="전자공학과">전자공학과</option>
                        <option value="정보컴퓨터공학과">정보컴퓨터공학과</option>
                        <option value="정치외교학과">정치외교학과</option>
                        <option value="조경학과">조경학과</option>
                        <option value="조선해양공학과">조선해양공학과</option>
                        <option value="조형학과">조형학과</option>
                        <option value="중어중문학과">중어중문학과</option>
                        <option value="지구과학교육과">지구과학교육과</option>
                        <option value="지리교육과">지리교육과</option>
                        <option value="지질환경과학과">지질환경과학과</option>
                        <option value="철학과">철학과</option>
                        <option value="체육교육과">체육교육과</option>
                        <option value="토목공학과">토목공학과</option>
                        <option value="통계학과">통계학과</option>
                        <option value="특수교육과">특수교육과</option>
                        <option value="한국음악학과">한국음악학과</option>
                        <option value="한문학과">한문학과</option>
                        <option value="항공우주공학과">항공우주공학과</option>
                        <option value="해양학과">해양학과</option>
                        <option value="행정학과">행정학과</option>
                        <option value="화공생명공학과">화공생명공학과</option>
                        <option value="환경공학과">환경공학과</option>
                        <option value="화학과">화학과</option>
                        <option value="화학교육과">화학교육과</option>
                        <option value="IT응용공학과">IT응용공학과</option>
					</select>
				</p>
			</div> 

		</fieldset>
	
		<fieldset>
			<legend>추가정보</legend>

			<div class="icon">
		    	<label class="cd-label" for="cd-name">지하철</label>
				<input type="text" name="cd-subway" id="cd-subway">
		    </div> 
			<div class="icon">
		    	<label class="cd-label" for="cd-name">자주가는 장소</label>
				<input type="text" name="cd-place" id="cd-place">
		    </div> 
			<div class="icon">
		    	<label class="cd-label" for="cd-name">강의</label>
				<input type="text" name="cd-class" id="cd-class">
		    </div> 
			
			<div>
		      	<input id="submit_final" type="submit" value="Send">
		    </div>
			
		</fieldset>
	</form>
<script src="js/jquery-2.1.1.js"></script>
<script src="js/main.js"></script> <!-- Resource jQuery -->
</body>
</html>