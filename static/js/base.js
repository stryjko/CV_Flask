/*global $, document */

function closeContainer(element, button) {
    "use strict";
    // Hides a section in the cv
    element.toggleClass("uk-hidden");
    button.toggleClass("uk-icon-plus-square-o uk-icon-minus-square-o");
}
