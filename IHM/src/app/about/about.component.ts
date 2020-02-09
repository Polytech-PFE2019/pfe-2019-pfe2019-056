import { Component, OnInit } from '@angular/core';
import {ServiceApi} from '../../service/service.api';
import {Router} from '@angular/router';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {

  request= {

    value:""
  };

  public  reponse
  //public champs=1
  //property = ['','hasChild','prop'];
  //constraint = ['2'];
  //pro: any;
  //cons: any;

  constructor(private serviceApi:ServiceApi,private router:Router) { }

  ngOnInit() {

  }

  ngAfterViewInit(){

    this.reponse=this.serviceApi.respnseUpload
    console.log(this.reponse)
  }


  onSubmit(f) {

    //var regex =/\?/gi;
    //var regex1 =/#/gi;
    //this.request=this.request.replace(regex,'\?')
    //this.request=this.request.replace(regex1,'\#')
    const formData = new FormData();
    formData.append('value',f['value'])

    console.log(f['value'])
    this.serviceApi.getResult(formData);
    this.router.navigate(['reponse']);

  }

  goToPage() {

    this.router.navigate(['form']);
  }


//  onOptionsSelected($event: Event) {

  //  this.champs=2
  //}

}
