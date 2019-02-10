var source_list = [{
  "name":"observatories",
  "node":"root",
  "values":[{
    "name":"SDO",
    "node":"parent",
    "values":[{
      "name":"instruments",
      "node":"parent",
      "values":[{
        "name":"AIA",
        "node":"child",
        "values":[{  
          "name":"measurements",
          "node":"parent",
          "values":[{
            "name":"Frequencies",
            "node":"child",
            "values": [{
              "id"  : "14",
              "name": "335"
            }, {
              "id":"10",
              "name":"171"
            }, {
               "id":"17",
               "name":"4500"
            }, {
               "id":"13",
               "name":"304"
            }, {
               "id":"9",
               "name":"131"
            }, {
               "id":"16",
               "name":"1700"
            }, {
               "id":"12",
               "name":"211"
            }, {
               "id":"15",
               "name":"1600"
            }, {
               "id":"8",
               "name":"94"
            }, {
               "id":"11",
               "name":"193"
            }]
          }]
        }]
      }, {
        "name":"HMI",
        "values":[{  
          "name":"measurement",
          "node":"parent",
          "values":[{
            "name":"Frequencies",
            "node":"child",
            "values": [{
              "id"  : "18",
              "name": "Continuum"
            }, {
              "id":"19",
              "name":"Magnetogram"
            }]
          }]
        }]
      }]
    }]
  }, {
    "name":"SOHO",
    "node":"parent",
    "values":[{
      "name":"instruments",
      "node":"parent",
      "values":[{
        "name":"EIT",
        "node":"child",
        "values":[{  
          "name":"measurements",
          "node":"parent",
          "values":[{
            "name":"Frequencies",
            "node":"child",
            "values": [{
              "id"  : "1",
              "name": "195"
            }, {
              "id":"3",
              "name":"304"
            }, {
               "id":"2",
               "name":"284"
            }, {
               "id":"0",
               "name":"171"
            }]
          }]
        }]
      }, {
        "name":"LASCO",
        "values":[{  
          "name":"measurement",
          "node":"parent",
          "values":[{
            "name":"Frequencies",
            "node":"child",
            "values":[{
              "id":"4",
              "name":"C2 White-Lite"
            }, {
              "id":"5",
              "name":"C3 White-Lite"
            }]
          }]
        }]
      }, {
        "name":"MDI",
        "values":[{  
          "name":"measurement",
          "node":"parent",
          "values":[{
            "name":"Frequencies",
            "node":"child",
            "values": [{
              "id":"7",
              "name": "Continuum"
            }, {
              "id":"6",
              "name":"Magnetogram"
            }]
          }]
        }]
      }]
    }]
  }, {
    "name":"STEREO_A",
    "node":"parent",
    "values":[{
      "name":"instruments",
      "node":"parent",
      "values":[{
        "name":"SECCHI",
        "node":"child",
        "values":[{  
          "name":"Detector",
          "values":[{
            "name":"EUVI",
            "node":"child",
            "values":[{
              "name":"Frequencies",
              "node":"child",
              "values": [{
                "id"  : "21",
                "name": "195"
              }, {
                "id":"23",
                "name":"304"
              }, {
                "id":"22",
                "name":"284"
              }, {
                "id":"20",
                "name":"171"
              }]
            }, {
              "name":"COR2",
              "node":"child",
              "values":[{
                "name":"Frequencies",
                "node":"child",
                "values": [{
                  "id"  : "29",
                  "name": "White-Lite"
                }]
              }]
            }, {
              "name":"COR1",
              "node":"child",
              "values":[{
                "name":"Frequencies",
                "node":"child",
                "values": [{
                  "id"  : "28",
                  "name": "White-Lite"
                }]
              }]
            }]
          }]
        }]
      }]
    }]
  }, {
    "name":"STEREO_B",
    "node":"parent",
    "values":[{
      "name":"instruments",
      "node":"parent",
      "values":[{
        "name":"SECCHI",
        "node":"child",
        "values":[{  
          "name":"Detector",
          "values":[{
            "name":"EUVI",
            "node":"child",
            "values":[{
              "name":"Frequencies",
              "node":"child",
              "values": [{
                "id"  : "25",
                "name": "195"
              }, {
                "id":"27",
                "name":"304"
              }, {
                "id":"26",
                "name":"284"
              }, {
                "id":"24",
                "name":"171"
              }]
            }, {
              "name":"COR1",
              "node":"child",
              "values":[{
                "name":"Frequencies",
                "node":"child",
                "values": [{
                  "id"  : "30",
                  "name": "White-Lite"
                }]
              }]
            }, {
              "name":"COR2",
              "node":"child",
              "values":[{
                "name":"Frequencies",
                "node":"child",
                "values": [{
                  "id"  : "31",
                  "name": "White-Lite"
                }]
              }]
            }]
          }]
        }]
      }]
    }]
  }]
}];