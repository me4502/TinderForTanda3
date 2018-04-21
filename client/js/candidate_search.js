
let venueId = ''
const myId = '2'

function getNextCard(id) {
  return new Promise((resolve, reject) => {
    $.get(`/get_next_card/${id}`, function(data) {
      const nextCard = JSON.parse(data)
      venueId = nextCard.id

      $('.swipeable-card').remove()

      const el = document.createElement('div')

      if (nextCard.message == 'none') {
        el.className = 'card blue-grey darken-1'
        el.innerHTML = `<div class="card-content white-text">
        <span class="card-title">No matches</span>
          <div class="body">
            Sorry, there have been no matches.
          </div>
        </div>`
        return resolve(el)
      }

      el.className = 'swipeable-card card blue-grey darken-1'
      el.innerHTML = `<div class="card-content white-text">
        <span class="card-title"> You've got an interested: ${nextCard.experience} </span>
          <div class="body">
            <div>
              <h2>Match</h2>
              <p>${ nextCard.name } </p>
            </div>
            <div>
              <h2>Localtion</h2>
              <p>${ nextCard.location } </p>
            </div>
            <div>
              <h2>Pay Range</h2>
              <p>${ nextCard.pay_range }</p>
            </div>
            <div>
              <h2>Hours</h2>
              <p>${ nextCard.hours } </p>
            </div>
            <div>
              <h2>Photo</h2>
              <img src="${ nextCard.photo }" style="width:100%; height: auto"></img>
            </div>
          </div>
        </div>`
      return resolve(el)
    })
  })
}

function doSwipe(direction) {
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
    $.post(`/swipe/${direction}/${myId}/${venueId}`, function() {
      $('.swipeable-card').removeClass('swipe-right')
      $('.swipeable-card').removeClass('swipe-left')
      $('.decline').removeClass('visible')
      $('.accept').removeClass('visible')

      getNextCard(myId).then(el => {
        $('.wrapper').append(el)
      })
    })
  }, 2300)
}

function getMatchedVenues() {
  return new Promise((resolve, reject) => {
    $.get(`/get_matched_venues/${myId}`, function(matches) {
      return resolve(matches)
    })
  })
}

function main() {

  window.addEventListener('keyup', event => {
    if (event.key == 'ArrowLeft') {
      doSwipe('left')
    }
    if (event.key == 'ArrowRight') {
      doSwipe('right')
    }
  })

  $(document).touchwipe({
    wipeLeft: () => { doSwipe('left') },
    wipeRight: () => { doSwipe('right') },
    min_move_x: 20,
    min_move_y: 20,
    preventDefaultEvents: true
  })

  getNextCard(myId).then(el => {
    $('.wrapper').append(el)
  })
}

$("document").ready(function(){
  $(".button-collapse").sideNav()
  main()
})