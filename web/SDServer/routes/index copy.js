var express = require('express');
var router = express.Router();
var webpush = require('web-push');

const vapidKeys = webpush.generateVAPIDKeys();
process.env.VAPID_PUBLIC_KEY = vapidKeys.publicKey;
process.env.VAPID_PRIVATE_KEY = vapidKeys.privateKey;

webpush.setVapidDetails(
    'http://192.168.31.55:3000/',
    process.env.VAPID_PUBLIC_KEY,
    process.env.VAPID_PRIVATE_KEY
);

router.get('/vapidPublicKey', function (req, res) {
  res.send(publicVapidKey);
});

router.post('/register', function (req, res) {
  res.sendStatus(201);
});

router.post('/sendNotification', function (req, res) {
  const subscription = req.body.subscription;
  webpush.sendNotification(subscription);
  // setTimeout(function () {
  //   webpush.sendNotification(subscription)
  //     .then(function () {
  //       res.sendStatus(201);
  //       console.log("성공")
  //     })
  //     .catch(function (error) {
  //       res.sendStatus(400);
  //       console.log(error);
  //     });

  // }, 3000);
});

module.exports = router;
