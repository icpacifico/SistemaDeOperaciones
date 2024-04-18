new DataTable('#example-table-bd',{
    language: {
        paginate: {
            first: '<span class="mdi mdi-chevron-double-left"></span>',
            last: '<span class="mdi mdi-chevron-double-right"></span>',
            next: '<span class="mdi mdi-chevron-right"></span>',
            previous: '<span class="mdi mdi-chevron-left"></span>'
        },
        url: '//cdn.datatables.net/plug-ins/2.0.4/i18n/es-CL.json',      
    },
    scrollX: true,
    scrollY: '50vh',
    pagingType: 'simple_numbers',
});