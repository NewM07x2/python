
// $jQuery(function(){

//   // hoverされた時に実行
//   $jQuery('.dropdwn .hover').hover(function(){
//       $jQuery(".ul:not(:animated)”, thishover_dropdwn_menu", jQuery(this)).slideDown();
//       alert("test");
//   }, function(){
//     alert("test");
//       $jQuery("ul.hover_dropdwn_menu",jQuery(this)).slideUp();
//   });

//   // hoverされた時に実行
//     $jQuery('.dropdwn .click').click(function(){
//       $jQuery("ul.click_dropdwn_menu", jQuery(this)).slideDown();
//   }, function(){
//       $jQuery("ul.click_dropdwn_menu",jQuery(this)).slideUp();
//   });

// });

$(function(){
  $('.dropdwn li').hover(function(){
      $("ul:not(:animated)", this).slideDown();
  }, function(){
      $("ul.dropdwn_menu",this).slideUp();
  });
});