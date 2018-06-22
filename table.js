        function loadTable() {
          var xhttp = new XMLHttpRequest();
          xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
             var obj = JSON.parse(this.responseText);
             /* check obj by setting breakpoint at this line */
            var thead_content = "";
            var tbody_content = "";

            thead_content += "<tr>";
            for(var i = 0; i < obj.fields.length; i++) {
              var head = obj.fields[i];
              thead_content += "<th>" + head.value + "</th>";
            }
            thead_content += "</tr>";

            for(var i = 0; i < obj.values.length; i++) {
              tbody_content += "<tr>";
              for(var j=0; j < obj.fields.length; j++){
                tbody_content += "<td>" + obj.values[i][obj.fields[j].key] + "</td>";
              }
              tbody_content += "</tr>";
            }

            document.getElementsByTagName("thead")[0].innerHTML = thead_content;
            document.getElementsByTagName("tbody")[0].innerHTML = tbody_content;
            }
          };
          xhttp.open("GET", "http://localhost:8080", true);
          xhttp.send();
        }

        function loadtest(){
            var thead_content = "";
            var tbody_content = "";

            thead_content += "<tr>";
            for(var i = 0; i < 3; i++) {
              thead_content += "<th>" + "앙제목띠" + "</th>";
            }
            thead_content += "</tr>";

            for(var i = 0; i < 5; i++) {
              tbody_content += "<tr>";
              for(var j=0; j < 3; j++){
                tbody_content += "<td>" + "앙내용띠" + "</td>";
              }
              tbody_content += "</tr>";
            }

            document.getElementsByTagName("thead")[0].innerHTML = thead_content;
            document.getElementsByTagName("tbody")[0].innerHTML = tbody_content;
        }