/**
 * 一个页面可以创建多个$.district对象
 */
(function (factory) {
    if (typeof define === "function" && define.amd) {
        // AMD. Register as an anonymous module.
        define(["jquery"], factory);
    } else {
        // Browser globals
        factory(jQuery);
    }

}(function ($) {
    $.fn.district = function (config) {
        return $.district.create(this, config);
    };

    jQuery.fn.outerHTML = function (s) {
        return s
            ? this.before(s).remove()
            : jQuery("<p>").append(this.eq(0).clone()).html();
    };

    var district_instance_counter = 0;

    $.district = {};

    $.district.create = function (element, config) {
        var tmp = new $.district.core();
        tmp.init(element, config);
        return tmp;
    };

    $.district.core = function () {
        this.id = district_instance_counter++;
    };

    $.district.core.config = {
        /**
         * html id
         */
        province_id: "province_",
        city_id: "city_",
        county_id: "county_",
        detail_id: "detail_",

        /**
         * html class
         */
        province_class: "",
        city_class: "",
        county_class: "",
        detail_class: "",

        /**
         * html style
         */
        province_style: "width:65px; height:24px; margin-right:20px;",
        city_style: "width:80px; height:24px; margin-right:20px;",
        county_style: "width:80px; height:24px; margin-right:20px;",
        detail_style: "width:200px; height: 18px;",

        /**
         * html style
         */
        province_selector_label: "省:",
        city_selector_label: "市:",
        county_selector_label: "县:",
        detail_label: "详细地址:"
    };

    $.district.core.prototype = {
        init: function (element, config) {
            if (!!!config) {
                config = {};
                this.config.province_id += this.id;
                this.config.city_id += this.id;
                this.config.county_id += this.id;
                this.config.detail_id += this.id;
            }
            this.config = $.extend(true, {}, $.district.core.config, config);
            this.element = element;

            this.province_select = $("<select></select>").attr("id", this.config.province_id).attr("name", this.config.province_id).attr("style", this.config.province_style).addClass(this.config.province_class);
            this.city_select = $("<select></select>").attr("id", this.config.city_id).attr("name", this.config.city_id).attr("style", this.config.city_style).addClass(this.config.city_class);
            this.county_select = $("<select></select>").attr("id", this.config.county_id).attr("name", this.config.county_id).attr("style", this.config.county_style).addClass(this.config.county_class);
            this.detail_input = $("<input/>").attr("id", this.config.detail_id).attr("name", this.config.detail_id).attr("style", this.config.detail_style).addClass(this.config.detail_class);

            this.province_select.append('<option value="' + -1 + '">--省--</option>');
            this.city_select.append('<option value="' + -1 + '">---市---</option>');
            this.county_select.append('<option value="' + -1 + '">---区---</option>');
        },

        __bind: function () {
            var $this = this;

            $("#" + $this.config.province_id).change(function () {
                var provinceId = $(this).val();
                $this.__add_options_by_parent_id(provinceId, $("#" + $this.config.city_id));
                $($this.element).trigger("province_change");
            });

            $("#" + $this.config.city_id).change(function () {
                var cityId = $(this).val();
                $this.__add_options_by_parent_id(cityId, $("#" + $this.config.county_id));
                $($this.element).trigger("city_change", [$("#" + $this.config.province_id).find("option:selected").text(), $("#" + $this.config.city_id).find("option:selected").text()]);
            });
        },

        __add_options_by_parent_id: function (parentId, subSelector, selectType) {
            $.ajax({
                type: 'GET',
                url: '/admin/op/district/' + parentId + "/children",
                dataType: 'json',
                async: false,
                success: function (data) {
                    var opts = eval(data);
                    var head_opt = subSelector.children()[0];
                    subSelector.empty();
                    subSelector.append(head_opt);
                    for (var i = 0; i < opts.length; i++) {
                        subSelector.append('<option value="' + opts[i]["id"] + '">' + opts[i]["name"] + '</option>');
                    }
                }
            });
        },

        __set: function (province, city, county, detail) {
            var $this = this;

            !!!province ? province = "" : $this.province_select.empty();
            !!!city ? city = "" : $this.city_select.empty();
            !!!county ? county = "" : $this.county_select.empty();
            !!!detail ? detail = "" : $this.detail_input.val(detail)

            $.ajax({
                type: 'GET',
                url: '/admin/op/district/get_options',
                dataType: 'json',
                async: false,
                data: {
                    "province": province,
                    "city": city,
                    "county": county
                },
                success: function (data) {
                    var jsonStr = eval(data);
                    var province_opts = jsonStr['provinces'];
                    if (!!province_opts) {
                        for (var i = 0; i < province_opts.length; i++) {
                            $this.province_select.append('<option value="' + province_opts[i]["id"] + '">' + province_opts[i]["name"] + '</option>');
                        }
                        if (!!province) {
                            $this.province_select.find("option:contains('" + province + "')").attr("selected", "selected");
                        }
                    }

                    var city_opts = jsonStr['cities'];
                    if (!!city_opts) {
                        for (var i = 0; i < city_opts.length; i++) {
                            $this.city_select.append('<option value="' + city_opts[i]["id"] + '">' + city_opts[i]["name"] + '</option>');
                        }
                        if (!!city) {
                            $this.city_select.find("option:contains('" + city + "')").attr("selected", "selected");
                        }
                    }

                    var county_opts = jsonStr['counties'];
                    if (!!county_opts) {
                        for (var i = 0; i < county_opts.length; i++) {
                            $this.county_select.append('<option value="' + county_opts[i]["id"] + '">' + county_opts[i]["name"] + '</option>');
                        }
                        if (!!county) {
                            $this.county_select.find("option:contains('" + county + "')").attr("selected", "selected");
                        }
                    }
                }
            });
        },

        render: function (deep, province, city, county, detail) {
            var $this = this;

            $this.__set(province, city, county, detail);

            if (deep == 1) {
                $(this.element).html($this.province_select.outerHTML());
            }

            if (deep == 2) {
                $(this.element).html($this.province_select.outerHTML() + $this.city_select.outerHTML());
            }

            if (deep == 3) {
                $(this.element).html($this.province_select.outerHTML() + $this.city_select.outerHTML() + $this.county_select.outerHTML());
            }

            if (deep == 4) {
                $(this.element).html($this.province_select.outerHTML() + $this.city_select.outerHTML() + $this.county_select.outerHTML() + $this.detail_input.outerHTML());
            }

            $this.__bind();

            return $($this.element);
        }
    };
}));
