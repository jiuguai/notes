function add_page(num){
	cp_child = $('.pagination>li:nth-last-child(2)').clone(true)
	cp_child.find('a').text(num)
	
	a = cp_child.find('a')
	a.attr('href',a.attr('href').replace(/\d+/,"123"))

	$('.pagination>li:nth-last-child(2)').after(cp_child)

} 


function add_pages(s_start, s_end, vip_num,e_start=0, e_end=-1){
	$('.x-right').text(`共有数据：${vip_num} 条`)
	for(page=s_start; page<=s_end; page++){
		add_page(page);
	}
	if (e_start!=0 ){
		add_page('...')
	}
	
	for(page=e_start; page<=e_end; page++){
		add_page(page);
	}

}




