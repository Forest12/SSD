var express = require('express');
var router = express.Router();
var admin = require('firebase-admin');
var serviceAccount = require('../fir-storage-sdk.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});


let tokens = ['esVf5XcwVAU:APA91bE58a5cX-ANlRmk9x1ZipvUjk8DhNr8EhdrOeTSRF8XlTM7oBvzHWCbxGkyayiE3C8oC7TNlKyiBQL2oOfiysWv3K-EAJ_-Y_v06uNAMdXakBREEpbL6ikc_zUzZuHC4QVLit8C'];
var payload = {
  notification:{
    title: "문앞에 낯선 사람이 있다",
    body: "누구게?"
  }
};

router.get('/', function(req, res) {
  admin.messaging().sendToDevice(tokens,payload)
  .then(function(response){
    console.log(response);
  })
  .catch(function(err){
    console.log(err);
  });
  res.json({ result : true });
});

module.exports = router;
