var express = require('express');
var router = express.Router();

router.get('/', function(req, res) {
  Resident.find(function (err, residents){
      if(err){
          return res.status(500).send({result: false});
      }
      res.json(residents);
  })
});

module.exports = router;
