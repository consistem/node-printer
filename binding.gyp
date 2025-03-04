{
  "variables": {
    "module_name%": "node_printer",
    "module_path%": "lib",
    "openssl_fips": "",
  },
  "targets": [
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    },
    {
      "target_name": "node_printer",
      "sources": [
        "<!@([\"python\", \"tools/getSourceFiles.py\", \"src\", \"cc\"])"
      ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ],
      "cflags_cc+": [
        "-Wno-deprecated-declarations",
        "-std=c++20"  # Adicionando suporte ao C++20
      ],
      "cflags+": [
        "-std=c++20",
        "<!(cups-config --cflags)"
      ],
      "conditions": [
        ["OS!='linux'", {"sources/": [["exclude", "_linux\\.cc$"]]}],
        ["OS!='mac'", {"sources/": [["exclude", "_mac\\.cc|mm?$"]]}],
        ["OS!='win'", {
          "sources/": [["exclude", "_win\\.cc$"]]}, {
          "sources/": [["exclude", "_posix\\.cc$"]]
        }],
        ["OS!='win'", {
          "cflags": [
            "<!(cups-config --cflags)",
            "-std=c++20"  # Adicionando suporte ao C++20
          ],
          "ldflags": [
            "<!(cups-config --libs)"
          ],
          "libraries": [
            "<!(cups-config --libs)"
          ],
          "link_settings": {
            "libraries": [
              "<!(cups-config --libs)"
            ]
          }
        }],
        ["OS=='mac'", {
          "cflags": [
            "-stdlib=libc++",
            "-std=c++20"  # Adicionando suporte ao C++20
          ],
          "xcode_settings": {
            "OTHER_CPLUSPLUSFLAGS": ["-std=c++20", "-stdlib=libc++"],
            "OTHER_LDFLAGS": ["-stdlib=libc++"],
            "MACOSX_DEPLOYMENT_TARGET": "10.7"
          }
        }]
      ]
    }
  ]
}