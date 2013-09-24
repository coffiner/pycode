$(document).ready(function(){
		$('.cat-item').mouseenter(function(){
			$(this).animate({paddingLeft: "6px"},"5");
		}).mouseout(function(){
			$(this).animate({paddingLeft: "0px"}, "1");
		})
	})