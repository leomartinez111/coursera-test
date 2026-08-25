function chooseRandomCategory (categories) {
  var randomIndex = Math.floor(Math.random() * categories.length);
  return categories[randomIndex];
}

// TODO: STEP 1: Build home page HTML based on the categories array
function buildAndShowHomeHTML (categories) {

  $ajaxUtils.sendGetRequest(
    homeHtmlUrl,
    function (homeHtml) {

      // TODO: STEP 2: Choose a random category
      var randomCategoryShortName = chooseRandomCategory(categories).short_name;

      // TODO: STEP 3: Substitute {{randomCategoryShortName}} with the chosen category
      var homeHtmlToInsertIntoPage = insertProperty(
        homeHtml, 
        "randomCategoryShortName", 
        "'" + randomCategoryShortName + "'"
      );

      // TODO: STEP 4: Insert the produced HTML into the main container
      insertHtml("#main-content", homeHtmlToInsertIntoPage);

    },
    false);
}