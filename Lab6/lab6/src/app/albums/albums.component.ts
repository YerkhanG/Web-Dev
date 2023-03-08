import { Component , OnInit} from '@angular/core';
import {Album} from "../models";
import {AlbumService} from "../album.service";
@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent {
  albums : Album[];
  constructor(private albumService : AlbumService){
    this.albums = [];
  }
  ngOnInit(): void {
    // console.log('ngOnInit');
    this.albumService.getAlbums().subscribe((albums) => {
      this.albums = albums;
    });
  }
  delete(album: Album): void {
    const index = this.albums.indexOf(album);
    if (index !== -1) {
      this.albums.splice(index, 1);
    }
  }
}
