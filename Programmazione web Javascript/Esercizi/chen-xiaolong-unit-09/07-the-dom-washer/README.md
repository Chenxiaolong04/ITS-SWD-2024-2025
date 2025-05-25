# YouTube DOM Access Exploration

This project explores the use of JavaScript DOM access methods to identify and interact with elements on the [YouTube homepage](https://www.youtube.com/). The goal is to extract at least 10 different DOM elements or collections using complex or specific selectors.

---
## DOM Access Examples

All JavaScript snippets were tested in the browser console (F12 or Ctrl+Shift+I > Console).

---

```js
//1. Video Title of the First Thumbnail
document.querySelector('ytd-rich-item-renderer h3 a#video-title')

//2.Channel Name Under First Video
document.querySelector('ytd-rich-item-renderer ytd-channel-name a')
//Explanation: Selects the channel name link under the first video card.

//3.All Sidebar Items
document.querySelectorAll('ytd-guide-section-renderer ytd-guide-entry-renderer a')
//Explanation: Selects all items in the sidebar, including "Home", "Shorts", "Subscriptions", etc.

//4.Search Input Field
document.querySelector('input#search')
//Explanation: The main search bar input field at the top of the page.

//5.Notifications Bell Icon
document.querySelector('ytd-notification-topbar-button-renderer button')
//Explanation: Targets the notifications button in the top-right corner.

//6.Sign In Button
document.querySelector('ytd-button-renderer.style-suggestive button')
//Explanation: Selects the "Sign in" button shown when not logged in.

//7.Video Cards Thumbnails (Collection)
document.querySelectorAll('ytd-rich-item-renderer ytd-thumbnail')
//Explanation: Selects all the thumbnail elements of video previews on the homepage.

//8.Hover Preview Containers (Video preview overlay)
document.querySelectorAll('ytd-thumbnail-overlay-time-status-renderer span')
//Explanation: Selects time-duration overlays shown on video thumbnails.

//9.Navigation Buttons in Sidebar (Icons only)
document.querySelectorAll('ytd-guide-entry-renderer tp-yt-paper-item yt-icon')
//Explanation: Grabs the icon-only elements for each nav button.

//10.YouTube Logo
document.querySelector('ytd-topbar-logo-renderer a#logo')
//Explanation: The clickable YouTube logo at the top-left.