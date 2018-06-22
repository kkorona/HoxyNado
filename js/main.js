jQuery(document).ready(function($){
	if( $('.floating-labels').length > 0 ) floatLabels();

	function floatLabels() {
		var inputFields = $('.floating-labels .cd-label').next();
		inputFields.each(function(){
			var singleInput = $(this);
			//check if user is filling one of the form fields 
			checkVal(singleInput);
			singleInput.on('change keyup', function(){
				checkVal(singleInput);	
			});
		});
	}

	function checkVal(inputField) {
		( inputField.val() == '' ) ? inputField.prev('.cd-label').removeClass('float') : inputField.prev('.cd-label').addClass('float');
	}
	

	
});	

$("#submit_final").click(function(){
	var data = new Object();
	data.name = $("#cd-name").val();
	data.sex = $("#radio-button").val();
	data.major = $("#major option:selected").val();
	data.year = $("#cd-year").val();
	data.subway = $("#cd-subway").val();
	data.place = $("#cd-place").val();
	data.subway = $("#cd-class").val();
	
	var jsonData = JSON.stringify(data, null, "\t");
	//$("input[name] : checked").val()
});
	
/*function checkValid(){
	var miss = [];
	var i=0;
	var miss_print = ""
	
	if($("#cd-name").val()==""){
		miss[i]="이름초성";
		i++;
	}
	if($("#cd-year").val()==""){
		miss[i]="학번";
		i++;
	}
	if($("#major option:selected").val()=="0"){
		miss[i]="학과";
		i++;
	}
	for(i=i-1; i>0; i--){
		miss_print += miss[i];
		miss_print += ", ";
	}
	miss_print += miss[0];
	
	return miss_print;
}*/