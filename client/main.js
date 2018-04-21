
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

}

$("document").ready(function(){
  $(".button-collapse").sideNav()
  main()
})