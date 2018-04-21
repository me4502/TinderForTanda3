
$("document").ready(function(){
  $(".button-collapse").sideNav()

  window.addEventListener('keyup', event => {
    if (event.key == 'ArrowLeft') {

      $('.swipeable-card').removeClass('swipe-right')
      $('.swipeable-card').addClass('swipe-left')
    }
    if (event.key == 'ArrowRight') {
      $('.swipeable-card').removeClass('swipe-left')
      $('.swipeable-card').addClass('swipe-right')
    }
  })
})