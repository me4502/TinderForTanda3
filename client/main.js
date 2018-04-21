
async function doSwipe(direction, id) {
  if (direction == 'left') {
    $('.swipeable-card').removeClass('swipe-right')
    $('.swipeable-card').addClass('swipe-left')

    $('.decline').addClass('visible')
  }

  if (direction == 'right') {
    $('.swipeable-card').removeClass('swipe-left')
    $('.swipeable-card').addClass('swipe-right')

    $('.accept').addClass('visible')
  }

  setTimeout(() => {
    $('.swipeable-card').removeClass('swipe-right')
    $('.swipeable-card').removeClass('swipe-left')
    $('.decline').removeClass('visible')
    $('.accept').removeClass('visible')
  }, 2500)

  // jQuery.post(`/swipe/${direction}/${id}`)

}

async function getNextCard(type) {
  return new Promise((resolve, reject) => {
    return resolve({ id: 0, title: 'Looking for bartender', body: 'We give big money' })
    // jQuery.get('/get_next_card/venue', data => {
    //   resolve(data)
    // })
  })
}

async function main() {
  const nextCard = await getNextCard('venue')

  const el = document.createElement('div')
  el.className = 'card-content white-text'
  el.innerHTML = `<span class="card-title"> ${ nextCard.title } </span>
    <div class="body">
      <p> ${ nextCard.body } </p>
    </div>`
  $('.swipeable-card').append(el)

  $('.swipeable-card').touchwipe({
    wipeLeft: () => { doSwipe('left') },
    wipeRight: () => { doSwipe('right') },
    min_move_x: 20,
    min_move_y: 20,
    preventDefaultEvents: true
  })

  window.addEventListener('keyup', event => {
    if (event.key == 'ArrowLeft') {
      doSwipe('left', nextCard.id)
    }
    if (event.key == 'ArrowRight') {
      doSwipe('right', nextCard.id)
    }
  })
}

$("document").ready(function(){
  $(".button-collapse").sideNav()
  main()
})