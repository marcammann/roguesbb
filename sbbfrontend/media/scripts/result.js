$(document).ready(
  function(){
    $('.result_container').hide();

    $('h3.result').click(function(){
      $(this).next('.result_container').slideToggle('fast');
      $(this).toggleClass('active');
      return false;
    });
    
    $('.result_container .block a.showall').click(function(){
      $(this).toggleClass('active');
      
      if ($(this).hasClass('active')) {
        $(this).text('hide all stopovers').next('table').find('tbody').addClass('showall');
      } else {
        $(this).text('show all stopovers').next('table').find('tbody').removeClass('showall');
      }
      return false;
    });
    
    $('table.stops tbody tr.showmore a').click(function(){
      $(this).parent().parent().parent().addClass('showall');
      return false;      
    });
  }
);