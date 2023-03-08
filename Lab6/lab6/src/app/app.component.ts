// import { Component, OnInit } from '@angular/core';
//
// import { IAlbum } from '../model/albums';
// import { AlbumService } from '../app/album.service';
// @Component({
//   selector: 'app-root',
//   templateUrl: './app.component.html',
//   styleUrls: ['./app.component.css']
// })
// export class AppComponent implements OnInit {
//   title = 'lab6';
//   albums: IAlbum[] =[];
//   constructor(private _albumService: AlbumService) { }
//   ngOnInit() {
//     this._albumService.getAllAlbums().subscribe({
//       next: albums =>{
//         this.albums=albums
//       }
//     })
//   }
// }
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'lab6';
}
