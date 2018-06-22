<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="org.json.simple.*" %>
<%@ page import="java.io.*" %>
<%@ page import="java.net.*" %>
<%@ page import="org.json.simple.JSONArray" %>
<%@ page import="org.json.simple.JSONObject" %>
<%@ page import="org.json.simple.parser.JSONParser" %>
<%@ page import="org.json.simple.parser.ParseException" %>
<%@ page import="java.util.Iterator" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<link href='http://fonts.googleapis.com/css?family=Open+Sans:400,300,700' rel='stylesheet' type='text/css'>
	<style>
        table {
            border-collapse: collapse;
            width: 90%;
        }
        th, td {
            text-align: left;
            padding: 8px;
        }
        tr:nth-child(even){background-color: #f2f2f2}
        thead {
            background-color: #4CAF50;
            color: white;
        }
    </style>
	<title>My Twinkles</title>

</head>
<body>
	<%
		java.lang.String name = request.getParameter("cd-name");
		java.lang.String sex = request.getParameter("radio-button");
		java.lang.String major = request.getParameter("major");
		java.lang.String year = request.getParameter("cd-year");
		java.lang.String subway = request.getParameter("cd-subway");
		java.lang.String place = request.getParameter("cd-place");
		java.lang.String Class = request.getParameter("cd-class");
		java.lang.String jsonStr = "{" +
				 		 "\"sex\":\"" + sex + "\"," + 
						 "\"name\":\"" + name + "\"," +
						 "\"year\":\"" + year + "\"," + 
						 "\"major\":\"" + major + "\"," + 
						 "\"subway\":\"" + subway + "\"," +
						 "\"place\":\"" + place + "\"," +
						 "\"class\":\"" + Class + "\"}";
		File objFile = new File("C:\\Users\\illak\\eclipse-workspace\\HoxyNado\\WebContent\\UserInfo.json");
      	BufferedWriter jsonO = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(objFile.getPath()), "UTF8"));

     	jsonO.write(jsonStr);

     	jsonO.close();
     	
     	try{

     	   ProcessBuilder pb = new ProcessBuilder("py","C:\\Users\\illak\\eclipse-workspace\\HoxyNado\\WebContent\\Finder.py");
     	   Process p = pb.start();
     	   p.waitFor();

     	}catch(java.lang.Exception e){System.out.println(e);}
     
     	%>
     	<div class="limiter">
     	<div class="container-table100">
     	<div class="wrap-table100">
     	<div class="table100 ver1 m-b-110">
     	<div class="table100-head">
     	
     	<%
     	JSONParser parser = new JSONParser();
     	 
    	try {
    		
    		java.lang.Object obj = parser.parse(new BufferedReader(new InputStreamReader(new FileInputStream("C:\\Users\\illak\\eclipse-workspace\\HoxyNado\\WebContent\\Articles.json"), "UTF-8")));
     
    		JSONObject jsonObject = (JSONObject) obj;
    		
    		JSONArray arr = (JSONArray)jsonObject.get("Articles");
    		
    		out.println("<table><thead><tr class=\"row100 head\"><th class=\"cell 100 column 1\">게시글명</th><th class=\"cell100 column2\">날짜</th></tr></thead></table>");
    		out.println("<div class=\"table100-body js-pscroll\"><table><tbody>");
    		int _size = arr.size();
    		for(int i=0; i<_size; i++) {
    			JSONObject tmp = (JSONObject) arr.get(i);
    			java.lang.String aid = (java.lang.String)tmp.get("aid");
    			java.lang.String articleTitle = (java.lang.String)tmp.get("articleTitle");
    			java.lang.String articleDate = (java.lang.String)tmp.get("articleDate");
    			out.println("<tr class=\"row100 body\">");
    			out.print("<td class=\"cell100 column1\"><a href = \"https://mypnu.net/sun/" + aid + "\"> " + articleTitle + "</a><td class=\"cell100 column2\"> " + articleDate + "</td></tr>");
    		}
    		out.println("</tbody></table></div>");
     
     
    	} catch (FileNotFoundException e) {
    		e.printStackTrace();
    	} catch (IOException e) {
    		e.printStackTrace();
    	} catch (ParseException e) {
    		e.printStackTrace();
    	}    	
     	
	   
	%>
	</div>
	</div>
	</div>
	</div>
	</div>
	<script src="WebContent/vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="WebContent/vendor/bootstrap/js/popper.js"></script>
	<script src="WebContent/vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="WebContent/vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="WebContent/vendor/perfect-scrollbar/perfect-scrollbar.min.js"></script>
	<script>
		$('.js-pscroll').each(function(){
			var ps = new PerfectScrollbar(this);

			$(window).on('resize', function(){
				ps.update();
			})
		});
			
		
	</script>
	<script src="WebContent/js/resultmain.js"></script>
	
</body>
</html>