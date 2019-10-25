var express = require('express');
var router = express.Router();
var Resident = require('../models/Resident');


router.get('/', function(req, res) {
    Resident.find(function (err, residents){
        if(err){
            return res.status(500).send({result: false});
        }
        res.json(residents);
    })
});

router.post('/', function(req, res){
    var resident = new Resident();
    resident.name = req.body.name;
    resident.age = req.body.age;
    resident.photo = req.body.photo;

    resident.save(function(err){
        if(err){
            return res.json({result : false})
        }
        res.json({result: true});
    });
});

module.exports = router;
  