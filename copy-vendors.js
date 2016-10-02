var copy = require('copy');

copy([
    "./bower_components/normalize.css/normalize.css",
    "./bower_components/milligram/dist/milligram.min.css",
    "./bower_components/milligram/dist/milligram.min.css.map"
],"./rdcom_website/static", {flatten: true});
