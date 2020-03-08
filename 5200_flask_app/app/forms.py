#Form classes can be declared here and imported into the routes view
#More to come soon
#This is the welcome page of our application where you make your selection and your request is processed.

<html>
 
  <body>
    <div class="main-block">
      <div class="left-part">
        
        <h1>International Address Form</h1>
        
      </div> 
 
      <form action="/result" method="post">
        <div class="title">
          <i class="fas fa-search"></i></i><h2> Please Select Country</h2>
        </div>
        <div class="info">
          <select name="country" id="country">
            <option value="">Country</option>
	       <option value = "1">Argentina</option>
               <option value = "2">Australia</option>
               <option value = "3">Austria</option>
               <option value = "4">Belgium</option>
	       <option value = "5">Brazil</option>
               <option value = "6">Canada</option>
               <option value = "7">Channel Islands</option>
               <option value = "8">Chile</option>
	       <option value = "9">China,PRC</option>
               <option value = "10">Costa Rica</option>
               <option value = "11">Crimea</option>
               <option value = "12">Czech Republic</option>
	       <option value = "13">Denmark</option>
               <option value = "14">Estonia</option>
               <option value = "15">Fiji</option>
               <option value = "16">Finland</option>
	       <option value = "17">Formosa</option>
               <option value = "18">France</option>
               <option value = "19">Germany</option>
               <option value = "20">Great Britain</option>
	       <option value = "21">Greenland</option>
               <option value = "22">Hong Kong</option>
               <option value = "23">Iceland</option>
               <option value = "24">India</option>
	       <option value = "25">Indonesia</option>
               <option value = "26">Ireland</option>
               <option value = "27">Isle of Man</option>
               <option value = "28">Israel</option>
	       <option value = "29">Italy</option>
               <option value = "30">Japan</option>
               <option value = "31">Korea</option>
               <option value = "32">Latvia</option>
	       <option value = "33">Luxembourg</option>
               <option value = "34">Malaysia</option>
               <option value = "35">Mexico</option>
               <option value = "36">Miscellaneous</option>
	       <option value = "37">Netherlands</option>
               <option value = "38">New Zealand</option>
               <option value = "39">Northern Island</option>
               <option value = "40">Norway</option>
	       <option value = "41">Oman</option>
               <option value = "42">Pakistan</option>
               <option value = "43">PRC</option>
               <option value = "44">Poland</option>
	       <option value = "45">Portugal</option>
	       <option value = "46">Puerto Rico</option>
               <option value = "47">Republic of China</option>
               <option value = "48">Romania</option>
               <option value = "49">Russia</option>
	       <option value = "50">Scotland</option>
	       <option value = "51">Scotland</option>
               <option value = "52">Singapore</option>
               <option value = "53">South Africa</option>
               <option value = "54">South Africa</option>
	       <option value = "55">South Korea</option>
               <option value = "56">Spain</option>
               <option value = "57">Sweden</option>
               <option value = "58">Switzerland</option>
	       <option value = "59">Taiwan</option>
               <option value = "60">U.K.</option>
               <option value = "61">Ukraine</option>
               <option value = "62">United Kingdom</option>	
	       <option value = "63">United States</option>
               <option value = "64">Uruguay</option>
               <option value = "65">Venezuela</option>
               <option value = "66">Wales</option>

               
            {% if countries %}
              {% for country in countries %}
                <option name={{ country }}>{{ country }}</option>
              {% endfor %}
            {% endif %}
          </select>
          <div class="addrItems" id="addrItems">
            <input type="text" name="name" temp_data="Street address" />
            <input type="text" name="name" temp_data="Street address line 2" />
            <input type="text" name="name" temp_data="City" />
            <input type="text" name="name" temp_data="Region" />
            <input type="text" name="name" temp_data="Postal / Zip code" />
          </div>
        </div>
        <button type="submit" href="">Search</button>
      </form>
    </div>
  </body>
<script type="text/javascript">

  $(document).ready(function() {

    $('#country').change(function() {
      var selectedCountry = $(this).children("option:selected").text();

      console.log(selectedCountry)

      $('#addrItems').empty();

      if (selectedCountry == "") {
        $('#addrItems').empty();

        $('#addrItems').append(
          '<input type="text" name="Street address" temp_data="Street address" />' + 
          '<input type="text" name="Street address line 2" temp_data="Street address line 2" />' + 
          '<input type="text" name="City" temp_data="City" />' +
          '<input type="text" name="Region" temp_data="Region" />' +
          '<input type="text" name="Postal/Zip code" temp_data="Postal/Zip code" />'
        );
        return;
      };

      $.ajax({
              type: 'post',
              url: '/format',
              data: {
                'country': selectedCountry
              },
              dataType: "json",
              success: function (data) {
                  console.log('Submission was successful.');
                  console.log(data);

                  lines = data[selectedCountry]

                  for (var line of lines) {
                    $('#addrItems').append('<div class="line">');

                    for (var item of line) {
                      if (item['name'] == 'postcode') {
                        $('#addrItems').append(
                          '<input type="text" name="' + item['name'] + '" temp_data="' + item['note'] + '" title="' + item['title'] + '"  pattern="' + item['pattern'] + '" required />'
                        ); 
                      } else {
                        $('#addrItems').append(
                          '<input type="text" name="' + item['name'] + '" temp_data="' + item['note'] + '" required />'
                        );
                      };
                    }
                    $('#addrItems').append('</div>');
                  };
              },
              error: function (data) {
                  console.log('An error occurred.');
                  console.log(data);
              }
          })
    });

  })

</script>
</html>
