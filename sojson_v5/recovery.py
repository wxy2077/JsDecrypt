#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
手动还原js代码
"""

import re
import execjs

source_js_code = """
    var nol_data = [[], [], []];
    var clideCount = 0;
    var isSend = ![];
    var touchHandler = function (_0x4ca7f8) {
      var _0x162621 = {
        xpUaV: _0x3574("0x0", "7ND["),
        mtSJG: _0x3574("0x1", "HF[@"),
        tppxc: function _0xe8ead(_0x4b0883, _0x665f4d) {
          return _0x4b0883 > _0x665f4d;
        },
        yECOB: "AGN",
        Bkfzz: "DEJ",
      };
      var _0x25eb36 = _0x162621["xpUaV"]["split"]("|"),
        _0x2bf820 = 0x0;
      while (!![]) {
        switch (_0x25eb36[_0x2bf820++]) {
          case "0":
            nol_data[clideCount]["push"](_0x321bff);
            continue;
          case "1":
            var _0x2ae4c7 =
              _0xe05337[_0x3574("0x2", "7$($")] ||
              _0xe05337[_0x3574("0x3", "7eVJ")] ||
              0x0;
            continue;
          case "2":
            console["log"](_0x2ae4c7, _0x197b3d, _0x25d9fa, _0x2b885c);
            continue;
          case "3":
            if (clideCount > 0x2) {
              if (
                _0x3574("0x4", "5dj(") !== _0x162621[_0x3574("0x5", "6*V3")]
              ) {
                return;
              } else {
              }
            }
            continue;
          case "4":
            var _0xe05337 = _0x314b79[0x0];
            continue;
          case "5":
            if (
              _0x162621[_0x3574("0x6", "i^lN")](
                nol_data[clideCount][_0x3574("0x7", "7$($")],
                0x3
              )
            ) {
              if (_0x162621["yECOB"] !== _0x162621[_0x3574("0x8", "vxFd")]) {
                return;
              } else {
                var _0x46d207 = _0x3574("0x9", "M3dg")[_0x3574("0xa", "7ND[")](
                    "|"
                  ),
                  _0x55c4f7 = 0x0;
                while (!![]) {
                  switch (_0x46d207[_0x55c4f7++]) {
                    case "0":
                      var _0x5ed316 =
                        _0x590194[_0x3574("0xb", "WA*a")] ||
                        _0x590194["webkitRadiusY"] ||
                        0x1;
                      continue;
                    case "1":
                      var _0x1172fb =
                        _0x590194[_0x3574("0xc", "7$($")] ||
                        _0x590194[_0x3574("0xd", "9ID*")] ||
                        0x1;
                      continue;
                    case "2":
                      _0x2c87c7["push"](_0x1172fb);
                      continue;
                    case "3":
                      nol_data[clideCount]["push"](_0x2c87c7);
                      continue;
                    case "4":
                      if (nol_data[clideCount][_0x3574("0xe", "B5kn")] > 0x3) {
                        return;
                      }
                      continue;
                    case "5":
                      if (_0x162621[_0x3574("0xf", "U3P$")](clideCount, 0x2)) {
                        return;
                      }
                      continue;
                    case "6":
                      _0x2c87c7[_0x3574("0x10", "bJ78")](_0x596eba);
                      continue;
                    case "7":
                      console[_0x3574("0x11", "[z)f")](
                        _0x596eba,
                        _0x1172fb,
                        _0x5ed316,
                        _0x45c010
                      );
                      continue;
                    case "8":
                      var _0x2c87c7 = [];
                      continue;
                    case "9":
                      _0x2c87c7[_0x3574("0x12", "n&K@")](_0x5ed316);
                      continue;
                    case "10":
                      var _0x590194 = _0x1ed165[0x0];
                      continue;
                    case "11":
                      _0x2c87c7["push"](_0x45c010);
                      continue;
                    case "12":
                      document["addEventListener"]("touchend", toucheEnd, ![]);
                      continue;
                    case "13":
                      var _0x596eba =
                        _0x590194[_0x3574("0x13", "cw2U")] ||
                        _0x590194[_0x3574("0x14", "5V86")] ||
                        0x0;
                      continue;
                    case "14":
                      var _0x1ed165 = _0x4ca7f8[_0x3574("0x15", "3@ob")];
                      continue;
                    case "15":
                      var _0x45c010 =
                        _0x590194[_0x3574("0x16", "z#gm")] ||
                        _0x590194[_0x3574("0x17", "M3dg")] ||
                        0x0;
                      continue;
                  }
                  break;
                }
              }
            }
            continue;
          case "6":
            _0x321bff["push"](_0x25d9fa);
            continue;
          case "7":
            var _0x25d9fa =
              _0xe05337[_0x3574("0x18", "6*V3")] ||
              _0xe05337[_0x3574("0x19", "!rML")] ||
              0x1;
            continue;
          case "8":
            _0x321bff["push"](_0x197b3d);
            continue;
          case "9":
            _0x321bff[_0x3574("0x1a", "i^lN")](_0x2ae4c7);
            continue;
          case "10":
            var _0x321bff = [];
            continue;
          case "11":
            _0x321bff["push"](_0x2b885c);
            continue;
          case "12":
            var _0x2b885c =
              _0xe05337["rotationAngle"] ||
              _0xe05337["webkitRotationAngle"] ||
              0x0;
            continue;
          case "13":
            var _0x314b79 = _0x4ca7f8["changedTouches"];
            continue;
          case "14":
            var _0x197b3d =
              _0xe05337[_0x3574("0x1b", "iC[M")] ||
              _0xe05337[_0x3574("0x1c", "gk&j")] ||
              0x1;
            continue;
          case "15":
            document["addEventListener"]("touchend", toucheEnd, ![]);
            continue;
        }
        break;
      }
    };
    function toucheEnd() {
      var _0x548286 = {
        CxlNv: _0x3574("0x1d", "7$($"),
        pWtIU: function _0x2010b7(_0x2dac09, _0x3bcf16) {
          return _0x2dac09 === _0x3bcf16;
        },
      };
      document[_0x3574("0x1e", "bJ78")](
        _0x548286[_0x3574("0x1f", "[Aq2")],
        touchHandler
      );
      clideCount += 0x1;
      if (_0x548286[_0x3574("0x20", "V7lF")](clideCount, 0x3)) {
        console[_0x3574("0x21", "aQOS")](nol_data);
        $["ajax"]({
          type: _0x3574("0x22", "z#gm"),
          url: nol_url,
          data: {
            user_id: userData[_0x3574("0x23", "ZRx9")],
            code: userData[_0x3574("0x24", "u2Zf")],
            data: nol_data,
            ua: navigator[_0x3574("0x25", "ZRx9")],
          },
          dataType: _0x3574("0x26", "*8u7"),
          success: function (_0x5bfacd) {},
        });
      }
    }
    document[_0x3574("0x27", "wTiq")]("touchstart", touchHandler, ![]);
    document[_0x3574("0x28", "V7lF")](
      _0x3574("0x29", "j$Aq"),
      function (_0x536df8) {
        var _0x3765a0 = {
          daLvE: _0x3574("0x2a", "[Aq2"),
          QtNKW: _0x3574("0x2b", "WA*a"),
        };
        document[_0x3574("0x2c", "v5W&")](_0x3765a0["daLvE"], toucheEnd);
        document["addEventListener"](_0x3765a0["QtNKW"], touchHandler, ![]);
      },
      ![]
    );
    (function (_0x383a8d, _0x3f11e7, _0x4deadf) {
      var _0x21f5b7 = {
        ddXbv: _0x3574("0x2d", "47y0"),
        HPUeF: function _0x1d89ce(_0x53584d, _0x5da508) {
          return _0x53584d !== _0x5da508;
        },
        yXOyc: _0x3574("0x2e", "Xacf"),
        TNFsv: function _0x12ca3f(_0x26ed1b, _0x161d03) {
          return _0x26ed1b === _0x161d03;
        },
        fZGCY: "sojson.v5",
        MDBrU: function _0xf96795(_0x527747, _0x1ba635) {
          return _0x527747 !== _0x1ba635;
        },
        YDwfm: _0x3574("0x2f", "U5y1"),
        IiYAe: _0x3574("0x30", "ys&E"),
        YRYZm: function _0x3703df(_0x191cac, _0x39f3bf) {
          return _0x191cac + _0x39f3bf;
        },
        OZDPx: _0x3574("0x31", "9ID*"),
        FTHuu: _0x3574("0x32", "U5y1"),
        OwupI: _0x3574("0x33", "aQOS"),
        QyZOJ: _0x3574("0x34", "$x1F"),
      };
      _0x4deadf = "al";
      try {
        _0x4deadf += _0x21f5b7[_0x3574("0x35", "[Aq2")];
        _0x3f11e7 = encode_version;
        if (
          !(
            _0x21f5b7[_0x3574("0x36", "u2Zf")](
              typeof _0x3f11e7,
              _0x21f5b7["yXOyc"]
            ) &&
            _0x21f5b7[_0x3574("0x37", "i^lN")](
              _0x3f11e7,
              _0x21f5b7[_0x3574("0x38", "$x1F")]
            )
          )
        ) {
          if (
            _0x21f5b7[_0x3574("0x39", "M3dg")](
              _0x21f5b7["YDwfm"],
              _0x21f5b7[_0x3574("0x3a", "aQOS")]
            )
          ) {
            _0x383a8d[_0x4deadf](
              _0x21f5b7[_0x3574("0x3b", "iC[M")](
                "删除",
                _0x3574("0x3c", "cw2U")
              )
            );
          } else {
            _0x383a8d[_0x4deadf](_0x21f5b7["OZDPx"]);
          }
        }
      } catch (_0xdc5e5a) {
        if (
          _0x21f5b7[_0x3574("0x3d", "9ID*")] ===
          _0x21f5b7[_0x3574("0x3e", "g9k3")]
        ) {
          _0x383a8d[_0x4deadf](_0x21f5b7[_0x3574("0x3f", "ys&E")]);
        } else {
          document[_0x3574("0x40", "n&K@")](
            _0x21f5b7[_0x3574("0x41", "i^lN")],
            touchHandler
          );
          clideCount += 0x1;
          if (_0x21f5b7[_0x3574("0x42", "Xacf")](clideCount, 0x3)) {
            console[_0x3574("0x43", "xn1D")](nol_data);
            $["ajax"]({
              type: _0x3574("0x44", "B5kn"),
              url: nol_url,
              data: {
                user_id: userData[_0x3574("0x45", "[z)f")],
                code: userData[_0x3574("0x46", "3@ob")],
                data: nol_data,
                ua: navigator["userAgent"],
              },
              dataType: _0x21f5b7[_0x3574("0x47", "7eVJ")],
              success: function (_0x1e5cc1) {},
            });
          }
        }
      }
    })(window);
    encode_version = "sojson.v5";
"""


# 获取执行js的函数
def get_js():
    f = open("./execute_func.js", 'r', encoding='utf-8')  # 打开JS文件
    line = f.readline()
    html_str = ''
    while line:
        html_str = html_str + line
        line = f.readline()
    return html_str


# 执行js 获取返回值
def encrypt(n1, n2):
    """

    :param n1:
    :param n2:
    :return:
    """
    js_str = get_js()
    ctx = execjs.compile(js_str)  # 加载JS文件
    # _0x3574 是上面js的函数名字 后面是两个参数
    return ctx.call('_0x3574', n1, n2)


# 正则匹配出整体这样的格式 [('_0x3574("0x0", "7ND[")', '0x0', '7ND[')， ("函数整体", "参数1", "参数2")]
res = re.findall(r"\[?(_0x3574\(\"(.*?)\", \"(.*?)\"\))\]?", source_js_code)

for i in res:
    # 获取执行后的结果
    new_i = encrypt(i[1], i[2])

    # 替换结果
    source_js_code = source_js_code.replace(i[0], f"\"{new_i}\"")

# 还原后的函数
print(source_js_code)


