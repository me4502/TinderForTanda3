
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

    jQuery.get('/get_next_card/venue', data => {
      console.log(data)
    })

    return resolve({
        id: 0,
        job_role: 'bartender',
        street_address: '1 Brunswick Street',
        suburb: 'Fortitude Valley',
        postcode: '4006',
        pay_range: '$20/hr - $30/hr',
        job_description: 'Friendly family owned and operated bar',
    })
  })
}

async function main() {
  const nextCard = await getNextCard('venue')

  const el = document.createElement('div')
  el.className = 'card-content white-text'
  el.innerHTML = `<span class="card-title">Looking for: ${ nextCard.job_role } </span>
    <div class="body">
      <div>
        <h2>Address</h2>
        <p>${ nextCard.street_address } ${ nextCard.suburb } ${ nextCard.postcode }</p>
      </div>
      <div>
        <h2>Pay Range</h2>
        <p>${ nextCard.pay_range }</p>
      </div>
      <div>
        <h2>Description</h2>
        <p>${ nextCard.job_description }</p>
      </div>
    </div>`
  $('.swipeable-card').append(el)

  $(document).touchwipe({
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