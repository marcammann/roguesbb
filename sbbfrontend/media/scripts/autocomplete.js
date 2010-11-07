$(document).ready(
  function() {
    var last = '';
    
    var field;
    var field1 = $("#id_station_from");
    var field2 = $("#id_station_to");
    
    var cont = $("#autocomplete_wrapper");
    var divac = null;
    var divac_css_id = 'autocomplete';
    var input = '';
    
    
    $(field1).attr('autocomplete', 'off').keydown(
      function(event) {
        controlKey(event);
      }
    );
    $(field1).keyup(
      function(event) {
        refreshSuggestions(event);
      }
    );
    $(field1).focusout(
      function(event) {
        field = null;
        hideBox();
      }
    );        
    $(field1).focusin(
      function(event) {
        field = $(field1);
      }
    );
    
    $(field2).attr('autocomplete', 'off').keydown(
      function(event) {
        field = $(field2);
        controlKey(event);
      }
    );
    $(field2).keyup(
      function(event) {
        refreshSuggestions(event);
      }
    );
    $(field2).focusout(
      function(event) {
        field = null;
        hideBox();
      }
    );        
    $(field2).focusin(
      function(event) {
        field = $(field2);
        refreshSuggestions(event);
      }
    );
    
    function setValue(value, text) {
      if (text) $(field).val(text);
      $('#'+$(field).attr('id')+'_station_id').val(value);
      
      console.log('#'+$(field).attr('id')+'_station_id');
      $(field).removeClass();
      if (value > 0) {
        $(field).addClass('ok');
      }
    }
    function checkState(event)
    {
      if (($(event.target).parents('#autocomplete').length !== 1) || $(event.target) !== $(field)) {
        hideBox();
      }
    }
    
    function hideBox() {
      $(cont).children('#'+divac_css_id).remove();
    }
    
    function selectItem(val) {
      divac = $(cont).children('#'+divac_css_id);
      if ($(divac).length) {
        var active = $(divac).find('ul li.result.active');
      
        if ($(active).length) {
          if (val == 1) active.next('li.result').addClass('active');
          else if (val == -1) active.prev('li.result').addClass('active');
          active.removeClass('active');
        } else {
          if (val == 1) $(divac).find('ul li.result:first').addClass('active');
          else if (val == -1) $(divac).find('ul li.result:last').addClass('active');        
        }
        
        active = $(divac).find('ul li.result.active');
        
        if (active.length) {
          setValue($(active).attr('id'), $(active).text());
        }
        else {
          setValue(0, last);
        }
      }
    }
    
    function controlKey(event) {
      var keys = {
        tab: 9,
        ret: 13,
        esc: 27,
        up: 38,
        down: 40
      };
      switch (event.keyCode) {
        case keys.up:
            event.preventDefault();
            selectItem(-1);
            break;
      
        case keys.down:
            event.preventDefault();
            selectItem(1);
            break;
          
        case keys.ret:
          event.preventDefault();
          var active = $(divac).find('ul li.result.active');
          hideBox();
          $(field).parent().next().children('input').focus();
          break;
          
        case keys.esc:
          event.preventDefault();
          setValue(0, last);
          hideBox();
          break;
      }
    }
    
    function refreshSuggestions(event) {
      var keys = {
        tab: 9,
        ret: 13,
        esc: 27,
        up: 38,
        down: 40
      };
      input = $(field).val();
      
      switch (event.keyCode) {
        case keys.up:
        case keys.down:
        case keys.ret:
        case keys.esc:
        case keys.tab:
          break;
        
        default:
          console.log('refesh for '+input);
          event.preventDefault();
          if (input != last) {
            last = input;
            
            if (input.length >= 1) {
              $(field).addClass('searching');
              
              $.getJSON(
                encodeURI("http://core01-eu.partiql.net:8002/sbb/1.0/stations.getFromString?callback=?"),
                {
                  station_query: input
                },
                function (data) {
                  setValue(0);
                  
                  divac = $(cont).children('#'+divac_css_id);
                  if (data.stations.length > 0) {
                    
                    var list = '';
                    list = '<ul>';
                    
                    var count=1;
                    var limit=10;
                    $.each(data.stations, function(i, obj) {
                      list += '<li class="result" id="'+obj.station_id+'">'+obj.station_name+'</li>';
                      if (i == limit) {
                        return false;
                      }
                    });
                    
                    if (data.stations.length == 1) {
                      console.log('set value because 1 result!');
                      var active = $(divac).find('ul li.result:first');
                      setValue($(active).attr('id'));
                    } else {
                      if (data.stations.length > limit) {
                        list += '<li>... '+(data.stations.length-limit)+' more results</li>';
                      }
                    }                  
                    
                    if ($(divac).length) {
                      $(divac).html(list);
                    } else {
                      var acclass='';
                      if ($(field).attr('id') == 'id_station_to') {
                        acclass='margin-top';
                      }
                      $(cont).append('<div id="'+divac_css_id+'" class="'+acclass+'">'+list+'</div>');
                    }
                    
                  }
                  else {
                    if ($(divac).length) {
                      hideBox();
                    }
                  }
                  
                  $(field).removeClass('searching');
                }
              );
              
            } else {
              hideBox();
            } 
          }
      }
    }
  }
);